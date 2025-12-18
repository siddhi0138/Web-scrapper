# DOM parsing example

from bs4 import BeautifulSoup
from typing import List, Dict


def parse_html(html: str) -> BeautifulSoup:
    """
    Parse HTML content into BeautifulSoup object.
    
    Args:
        html: HTML content as string
    
    Returns:
        BeautifulSoup object
    """
    return BeautifulSoup(html, 'html.parser')


def extract_elements(html: str, selector: str) -> List:
    """
    Extract elements using CSS selector.
    
    Args:
        html: HTML content
        selector: CSS selector
    
    Returns:
        List of matching elements
    """
    soup = parse_html(html)
    return soup.select(selector)


def extract_text(html: str, selector: str) -> List[str]:
    """
    Extract text content using CSS selector.
    
    Args:
        html: HTML content
        selector: CSS selector
    
    Returns:
        List of text content
    """
    elements = extract_elements(html, selector)
    return [elem.get_text(strip=True) for elem in elements]


def extract_attributes(html: str, selector: str, attribute: str) -> List[str]:
    """
    Extract attribute values using CSS selector.
    
    Args:
        html: HTML content
        selector: CSS selector
        attribute: Attribute name to extract
    
    Returns:
        List of attribute values
    """
    elements = extract_elements(html, selector)
    return [elem.get(attribute) for elem in elements if elem.get(attribute)]


def dom_to_dict(element) -> Dict:
    """
    Convert DOM element to dictionary.
    
    Args:
        element: BeautifulSoup element
    
    Returns:
        Dictionary representation
    """
    result = {
        'tag': element.name,
        'text': element.get_text(strip=True),
        'attributes': dict(element.attrs) if element.attrs else {}
    }
    return result


if __name__ == "__main__":
    # Example usage
    sample_html = """
    <html>
        <body>
            <div class="item">
                <h2>Item 1</h2>
                <p>Description 1</p>
            </div>
            <div class="item">
                <h2>Item 2</h2>
                <p>Description 2</p>
            </div>
        </body>
    </html>
    """
    
    texts = extract_text(sample_html, "div.item h2")
    print("Extracted titles:", texts)
