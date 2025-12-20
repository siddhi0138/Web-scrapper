"""
Aggregated scraper for multiple job sources.

Combines results from all individual scrapers and manages data export.
"""

import json
import logging
from typing import List, Dict, Any
from pathlib import Path

from google_careers import GoogleCareersScraper
from microsoft_careers import MicrosoftCareersScraper
from amazon_jobs import AmazonJobsScraper

logger = logging.getLogger(__name__)


class AggregatedScraper:
    """Coordinates scraping from multiple sources."""

    def __init__(self):
        """Initialize the aggregated scraper."""
        self.logger = logger
        self.scrapers = [
            GoogleCareersScraper(),
            MicrosoftCareersScraper(),
            AmazonJobsScraper(),
        ]

    def scrape_all(self) -> List[Dict[str, Any]]:
        """
        Run all scrapers and aggregate results.

        Returns:
            Combined list of all jobs from all sources
        """
        all_jobs = []

        for scraper in self.scrapers:
            try:
                jobs = scraper.scrape()
                all_jobs.extend(jobs)
                self.logger.info(f"Added {len(jobs)} jobs from {scraper.__class__.__name__}")
            except Exception as e:
                self.logger.error(f"Error with {scraper.__class__.__name__}: {str(e)}")

        self.export_jobs(all_jobs)
        return all_jobs

    def export_jobs(self, jobs: List[Dict[str, Any]]):
        """
        Export jobs to JSON file.

        Args:
            jobs: List of job dictionaries to export
        """
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "jobs.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(jobs, f, indent=2, ensure_ascii=False)
            self.logger.info(f"Exported {len(jobs)} jobs to {output_file}")
        except Exception as e:
            self.logger.error(f"Error exporting jobs: {str(e)}")
