# src/infrastructure/scraper/scrape.py

import argparse
import json
import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.models.scraped_resource import ScrapedResource
from src.infrastructure.db.session import AsyncSessionLocal
from src.utils.logger import get_logger

logger = get_logger(__name__)
OUTPUT_FILE = Path("samples/scraped.json")


async def scrape_quotes(page: int = 1):
    """Scrape quotes from quotes.toscrape.com"""
    url = f"http://quotes.toscrape.com/page/{page}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, "html.parser")

            quotes = []
            for quote in soup.select(".quote"):
                text = quote.select_one(".text").get_text(strip=True)
                author = quote.select_one(".author").get_text(strip=True)
                quotes.append(
                    {
                        "title": text,
                        "author": author,
                        "source_url": url,
                        "content": text,
                    }
                )
            return quotes


async def run_scraper(pages: int = 1, save_db: bool = False):
    all_data = []
    for page in range(1, pages + 1):
        quotes = await scrape_quotes(page)
        if not quotes:
            break
        all_data.extend(quotes)

    # Save JSON
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    logger.info(f"Scraped {len(all_data)} items → {OUTPUT_FILE}")

    if save_db:
        async with AsyncSessionLocal() as session:
            for item in all_data:
                resource = ScrapedResource(
                    title=item["title"],
                    author=item.get("author"),
                    source_url=item["source_url"],
                    content=item["content"],
                )
                session.add(resource)
            await session.commit()
        logger.info(f"Inserted {len(all_data)} items into DB.")

    return all_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EduFlow Scraper")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--db", action="store_true", help="Save results to database")
    args = parser.parse_args()

    import asyncio
    asyncio.run(run_scraper(args.pages, args.db))
