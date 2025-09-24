# src/interfaces/cli/__main__.py

import argparse
import asyncio
from src.infrastructure.scraper.scrape import run_scraper


def main():
    parser = argparse.ArgumentParser(description="EduFlow CLI")
    parser.add_argument("scrape", help="Run scraper", nargs="?")
    parser.add_argument("--pages", type=int, default=1, help="Number of pages")
    parser.add_argument("--db", action="store_true", help="Save results to DB")
    args = parser.parse_args()

    if args.scrape:
        asyncio.run(run_scraper(pages=args.pages, save_db=args.db))


if __name__ == "__main__":
    main()
