"""
Main scheduler and orchestrator for job market intelligence scraper.

Coordinates the scraping of multiple job sources and aggregates results.
"""

import logging
from datetime import datetime
from logging.logger import setup_logger

# Configure logging
logger = setup_logger(__name__)


class JobMarketScheduler:
    """Orchestrates job scraping and analysis tasks."""

    def __init__(self):
        """Initialize the scheduler."""
        self.logger = logger
        self.scraped_jobs = []

    def run_all_scrapers(self):
        """Execute all job market scrapers."""
        self.logger.info("Starting job market scraping cycle")
        # Import scrapers dynamically
        try:
            from experiments.aggregate_scraper import AggregatedScraper
            scraper = AggregatedScraper()
            self.scraped_jobs = scraper.scrape_all()
            self.logger.info(f"Successfully scraped {len(self.scraped_jobs)} jobs")
        except Exception as e:
            self.logger.error(f"Error during scraping: {str(e)}")

    def run_analytics(self):
        """Run analytics on collected data."""
        self.logger.info("Running analytics on job data")
        try:
            from analytics.skill_trends import SkillAnalyzer
            analyzer = SkillAnalyzer(self.scraped_jobs)
            analyzer.analyze()
            self.logger.info("Analytics completed successfully")
        except Exception as e:
            self.logger.error(f"Error during analytics: {str(e)}")

    def execute(self):
        """Execute the full scraping and analysis pipeline."""
        self.logger.info(f"Pipeline execution started at {datetime.now()}")
        self.run_all_scrapers()
        self.run_analytics()
        self.logger.info(f"Pipeline execution completed at {datetime.now()}")


if __name__ == "__main__":
    scheduler = JobMarketScheduler()
    scheduler.execute()
