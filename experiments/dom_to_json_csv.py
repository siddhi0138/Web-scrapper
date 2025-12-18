# Convert DOM data to JSON and CSV

import json
import csv
from typing import List, Dict
from bs4 import BeautifulSoup


def dom_to_json(elements: List, output_file: str = None) -> str:
    """
    Convert DOM elements to JSON format.
    
    Args:
        elements: List of BeautifulSoup elements
        output_file: Optional file path to save JSON
    
    Returns:
        JSON string
    """
    data = []
    for elem in elements:
        item = {
            'tag': elem.name,
            'text': elem.get_text(strip=True),
            'attributes': dict(elem.attrs) if elem.attrs else {}
        }
        data.append(item)
    
    json_str = json.dumps(data, indent=2)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(json_str)
    
    return json_str


def dom_to_csv(data: List[Dict], output_file: str = None) -> str:
    """
    Convert structured data to CSV format.
    
    Args:
        data: List of dictionaries
        output_file: Optional file path to save CSV
    
    Returns:
        CSV string
    """
    if not data:
        return ""
    
    keys = data[0].keys()
    
    csv_lines = []
    csv_lines.append(','.join(keys))
    
    for row in data:
        values = []
        for key in keys:
            value = row.get(key, '')
            # Escape quotes and wrap in quotes if contains comma
            if isinstance(value, str) and ',' in value:
                value = f'"{value.replace(chr(34), chr(34) + chr(34))}"'
            values.append(str(value))
        csv_lines.append(','.join(values))
    
    csv_str = '\n'.join(csv_lines)
    
    if output_file:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            f.write(csv_str)
    
    return csv_str


def parse_and_export(html: str, selector: str, format: str = 'json', output_file: str = None):
    """
    Parse HTML and export data in specified format.
    
    Args:
        html: HTML content
        selector: CSS selector for elements
        format: 'json' or 'csv'
        output_file: Output file path
    """
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(selector)
    
    if format == 'json':
        return dom_to_json(elements, output_file)
    elif format == 'csv':
        data = [
            {
                'tag': elem.name,
                'text': elem.get_text(strip=True)
            }
            for elem in elements
        ]
        return dom_to_csv(data, output_file)


if __name__ == "__main__":
    # Example usage
    sample_html = """
    <html>
        <body>
            <article class="post">
                <h1>Title 1</h1>
                <p class="content">Content 1</p>
            </article>
            <article class="post">
                <h1>Title 2</h1>
                <p class="content">Content 2</p>
            </article>
        </body>
    </html>
    """
    
    json_output = parse_and_export(sample_html, 'article.post', 'json')
    print("JSON Output:")
    print(json_output)
