# Job Market Intelligence Scraper v2

A comprehensive web scraping system for collecting and analyzing job market data from major tech companies.

## Overview

This project aggregates job listings from multiple tech career pages and provides analytics on skills trends, hiring patterns, and market intelligence.

## Features

- Multi-source job scraping (Google, Microsoft, Amazon, etc.)
- Skill trend analysis and visualization
- Structured logging and error handling
- Ethical compliance and robots.txt adherence
- JSON export and CSV analytics

## Project Structure

```
job-market-intelligence-scraper-v2/
├── README.md
├── scheduler.py           # Main orchestrator and scheduling logic
├── logging/
│   └── logger.py         # Centralized logging configuration
├── experiments/
│   ├── google_careers.py # Google careers scraper
│   ├── microsoft_careers.py # Microsoft careers scraper
│   ├── amazon_jobs.py    # Amazon jobs scraper
│   └── aggregate_scraper.py # Unified scraping interface
├── analytics/
│   └── skill_trends.py   # Skill analysis and trending
├── output/
│   ├── jobs.json        # Raw job data
│   └── skill_trends.csv # Analyzed trends
└── ethics-and-compliance/
    └── notes.md         # Legal and ethical guidelines
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scheduler.py
```

## Data Output

- `output/jobs.json`: Structured job listing data
- `output/skill_trends.csv`: Skill frequency and trends

## Compliance

See `ethics-and-compliance/notes.md` for legal considerations and ethical guidelines.
