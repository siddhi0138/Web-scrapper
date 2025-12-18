# JavaScript rendering example using Playwright

import asyncio
from playwright.async_api import async_playwright
from typing import Optional


async def render_page(url: str, wait_selector: Optional[str] = None) -> str:
    """
    Render page with JavaScript execution.
    
    Args:
        url: URL to render
        wait_selector: Optional selector to wait for
    
    Returns:
        Rendered HTML content
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until='networkidle')
            
            # Wait for specific element if provided
            if wait_selector:
                await page.wait_for_selector(wait_selector)
            
            content = await page.content()
            return content
        finally:
            await browser.close()


async def extract_rendered_data(url: str, selector: str) -> list:
    """
    Extract data from JavaScript-rendered content.
    
    Args:
        url: URL to scrape
        selector: CSS selector for elements
    
    Returns:
        List of text content from elements
    """
    from bs4 import BeautifulSoup
    
    html = await render_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(selector)
    
    return [elem.get_text(strip=True) for elem in elements]


async def take_screenshot(url: str, output_file: str):
    """
    Take screenshot of rendered page.
    
    Args:
        url: URL to screenshot
        output_file: Path to save screenshot
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until='networkidle')
            await page.screenshot(path=output_file)
            print(f"Screenshot saved to {output_file}")
        finally:
            await browser.close()


async def get_page_metrics(url: str) -> dict:
    """
    Get page performance metrics.
    
    Args:
        url: URL to analyze
    
    Returns:
        Dictionary with metrics
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until='networkidle')
            metrics = await page.metrics()
            return metrics
        finally:
            await browser.close()


if __name__ == "__main__":
    # Example usage
    print("Note: Requires 'pip install playwright' and 'playwright install'")
    print("Uncomment to run examples")
    
    # asyncio.run(render_page("https://example.com"))
    # asyncio.run(take_screenshot("https://example.com", "screenshot.png"))
