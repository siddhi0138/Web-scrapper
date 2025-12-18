# Basic HTTP request example

import requests


def fetch_webpage(url: str) -> str:
    """
    Fetch a webpage using HTTP GET request.
    
    Args:
        url: URL to fetch
    
    Returns:
        Response text
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    return response.text


def fetch_json_api(url: str) -> dict:
    """
    Fetch JSON from API endpoint.
    
    Args:
        url: API endpoint URL
    
    Returns:
        JSON response as dictionary
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    return response.json()


if __name__ == "__main__":
    # Example usage
    try:
        html = fetch_webpage("https://example.com")
        print(f"Fetched {len(html)} characters")
    except requests.RequestException as e:
        print(f"Error: {e}")
