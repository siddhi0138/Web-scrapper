"""
Analytics module for analyzing skill trends in job market data.

Processes job listings to identify trending skills and create reports.
"""

import json
import logging
from typing import List, Dict, Any
from collections import Counter
from pathlib import Path
import csv

logger = logging.getLogger(__name__)


class SkillAnalyzer:
    """Analyzes skills trends from job data."""

    def __init__(self, jobs: List[Dict[str, Any]]):
        """
        Initialize the skill analyzer.

        Args:
            jobs: List of job dictionaries with skills information
        """
        self.logger = logger
        self.jobs = jobs
        self.skill_counts = Counter()

    def extract_skills(self):
        """Extract and count skills from job listings."""
        self.logger.info("Extracting skills from job data")

        for job in self.jobs:
            if 'skills' in job:
                skills = job['skills']
                if isinstance(skills, list):
                    self.skill_counts.update(skills)
                elif isinstance(skills, str):
                    self.skill_counts.update(skill.strip() for skill in skills.split(','))

        self.logger.info(f"Extracted skills from {len(self.jobs)} jobs")

    def analyze(self):
        """Run complete skill analysis pipeline."""
        self.logger.info("Starting skill trend analysis")
        self.extract_skills()
        self.generate_report()

    def generate_report(self):
        """Generate and export skill trend report."""
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "skill_trends.csv"

        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Skill', 'Frequency'])

                for skill, count in self.skill_counts.most_common():
                    writer.writerow([skill, count])

            self.logger.info(f"Skill trends report exported to {output_file}")
        except Exception as e:
            self.logger.error(f"Error generating report: {str(e)}")
