# tests/integration/test_scraper.py
import pytest
import asyncio
from pathlib import Path
from src.infrastructure.scraper.scrape import run_scraper

@pytest.mark.asyncio
async def test_scraper_json_output(tmp_path):
    output_file = tmp_path / "scraped.json"
    data = await run_scraper(pages=1, save_db=False)
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]
