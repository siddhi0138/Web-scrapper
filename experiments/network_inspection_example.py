# Network inspection example

import asyncio
from playwright.async_api import async_playwright


async def capture_network_requests(url: str) -> list:
    """
    Capture all network requests made by page.
    
    Args:
        url: URL to monitor
    
    Returns:
        List of request details
    """
    requests_list = []
    
    async def handle_request(request):
        requests_list.append({
            'url': request.url,
            'method': request.method,
            'resource_type': request.resource_type,
            'headers': dict(request.headers)
        })
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        page.on("request", handle_request)
        
        try:
            await page.goto(url, wait_until='networkidle')
            return requests_list
        finally:
            await browser.close()


async def monitor_api_calls(url: str) -> list:
    """
    Monitor API/AJAX calls made by JavaScript.
    
    Args:
        url: URL to monitor
    
    Returns:
        List of API call details
    """
    api_calls = []
    
    async def handle_response(response):
        # Filter for API responses
        if 'api' in response.url or response.url.endswith(('.json', '.xml')):
            try:
                body = await response.text()
            except:
                body = None
            
            api_calls.append({
                'url': response.url,
                'status': response.status,
                'content_type': response.headers.get('content-type'),
                'body_preview': body[:200] if body else None
            })
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        page.on("response", handle_response)
        
        try:
            await page.goto(url, wait_until='networkidle')
            return api_calls
        finally:
            await browser.close()


async def get_network_waterfall(url: str) -> dict:
    """
    Analyze network timing and performance.
    
    Args:
        url: URL to analyze
    
    Returns:
        Network timing information
    """
    timing_data = {
        'requests': [],
        'total_time': 0
    }
    
    async def handle_request(request):
        timing_data['requests'].append({
            'url': request.url,
            'method': request.method,
            'type': request.resource_type
        })
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        page.on("request", handle_request)
        
        try:
            start_time = asyncio.get_event_loop().time()
            await page.goto(url, wait_until='networkidle')
            end_time = asyncio.get_event_loop().time()
            
            timing_data['total_time'] = end_time - start_time
            return timing_data
        finally:
            await browser.close()


if __name__ == "__main__":
    print("Note: Requires 'pip install playwright' and 'playwright install'")
    print("Uncomment to run examples")
    
    # result = asyncio.run(capture_network_requests("https://example.com"))
    # print(f"Captured {len(result)} requests")
