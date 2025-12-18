# HTTP request with retry logic

import requests
import time
from typing import Optional


class RetryableHTTPClient:
    """HTTP client with retry and backoff logic."""
    
    def __init__(self, max_retries: int = 3, backoff_factor: float = 2.0, timeout: int = 10):
        """
        Initialize retryable HTTP client.
        
        Args:
            max_retries: Maximum number of retries
            backoff_factor: Exponential backoff factor
            timeout: Request timeout in seconds
        """
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get(self, url: str, **kwargs) -> Optional[requests.Response]:
        """
        GET request with retry logic.
        
        Args:
            url: URL to fetch
            **kwargs: Additional arguments for requests.get
        
        Returns:
            Response object or None if all retries failed
        """
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, timeout=self.timeout, **kwargs)
                response.raise_for_status()
                return response
            
            except requests.RequestException as e:
                if attempt == self.max_retries - 1:
                    print(f"Failed after {self.max_retries} attempts: {e}")
                    return None
                
                wait_time = self.backoff_factor ** attempt
                print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s: {e}")
                time.sleep(wait_time)
    
    def post(self, url: str, **kwargs) -> Optional[requests.Response]:
        """
        POST request with retry logic.
        
        Args:
            url: URL to send request to
            **kwargs: Additional arguments for requests.post
        
        Returns:
            Response object or None if all retries failed
        """
        for attempt in range(self.max_retries):
            try:
                response = self.session.post(url, timeout=self.timeout, **kwargs)
                response.raise_for_status()
                return response
            
            except requests.RequestException as e:
                if attempt == self.max_retries - 1:
                    print(f"Failed after {self.max_retries} attempts: {e}")
                    return None
                
                wait_time = self.backoff_factor ** attempt
                print(f"Attempt {attempt + 1} failed, retrying in {wait_time}s: {e}")
                time.sleep(wait_time)


if __name__ == "__main__":
    # Example usage
    client = RetryableHTTPClient(max_retries=3, backoff_factor=2.0)
    
    response = client.get("https://example.com")
    if response:
        print(f"Success! Status: {response.status_code}")
        print(f"Content length: {len(response.text)}")
