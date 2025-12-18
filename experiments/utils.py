# Utility functions for web data extraction

import time
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def retry_request(func, max_retries: int = 3, backoff_factor: float = 2.0):
    """
    Retry a function with exponential backoff.
    
    Args:
        func: Function to retry
        max_retries: Maximum number of retries
        backoff_factor: Factor to multiply wait time by
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = backoff_factor ** attempt
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s: {e}")
            time.sleep(wait_time)


def rate_limit(requests_per_second: float = 1.0):
    """
    Rate limit decorator.
    
    Args:
        requests_per_second: Number of requests allowed per second
    """
    def decorator(func):
        last_called = [0.0]
        
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = (1.0 / requests_per_second) - elapsed
            
            if wait_time > 0:
                time.sleep(wait_time)
            
            last_called[0] = time.time()
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


def extract_data(html: str, selector: str, attribute: Optional[str] = None) -> list:
    """
    Extract data from HTML using CSS selector.
    
    Args:
        html: HTML content
        selector: CSS selector
        attribute: Optional attribute to extract
    
    Returns:
        List of extracted data
    """
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(selector)
    
    if attribute:
        return [elem.get(attribute) for elem in elements]
    else:
        return [elem.get_text(strip=True) for elem in elements]
