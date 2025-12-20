# LLM-Powered Data Extraction

## Overview
Large Language Models (LLMs) have revolutionized data extraction by replacing brittle CSS/XPath selectors with semantic understanding. They can reason about page content, generate extraction logic, and adapt to layout changes automatically.

## Key LLM Capabilities for Scraping

### 1. Semantic Understanding
- Understand content meaning, not just structure
- Extract even when HTML structure changes
- Reason about relationships and hierarchies

### 2. Natural Language Extraction Prompts
```
"Extract all product titles and prices in JSON format"
```
Instead of:
```
div.product > h2, div.product > span.price
```

### 3. Selector Generation
- LLM analyzes DOM and generates appropriate CSS/XPath
- Automatically regenerates on failures
- Learns from multiple site examples

### 4. Form Understanding
- Auto-detect form fields and their purposes
- Suggest appropriate values (email format, date, etc.)
- Handle complex multi-step forms

### 5. Contextual Navigation
- Understand navigation intent ("Go to next page")
- Handle site-specific patterns ("Click product thumbnail")
- Reason about button purposes

## Integration Patterns

### Pattern 1: Prompt-Based Extraction
```python
from openai import OpenAI

def extract_with_llm(html: str, task: str):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": f"""
                Extract data from this HTML: {task}
                Return as JSON array.
                """,
            }
        ]
    )
    return response.choices[0].message.content
```

### Pattern 2: LLM-Generated Selectors
```python
def generate_selectors(html: str, target: str):
    """LLM generates CSS selectors for target elements"""
    prompt = f"""
    Given this HTML structure, generate CSS selectors to extract: {target}
    Return ONLY valid CSS selectors, one per line.
    """
    selectors = llm_call(prompt, html)
    return selectors.split('\n')
```

### Pattern 3: Self-Healing Scraper
```python
def robust_extract(url: str, selector: str, llm_model):
    try:
        # Try selector
        return extract_with_selector(url, selector)
    except SelectorNotFound:
        # LLM regenerates selector
        new_selector = llm_model.regenerate_selector(
            url=url,
            original_selector=selector,
            error="selector_not_found"
        )
        return extract_with_selector(url, new_selector)
```

## Supported LLM Models

### Vision-Capable (Multimodal)
- **GPT-4V**: Strong visual understanding
- **Claude 3 Vision**: Excellent reasoning
- **Gemini Pro Vision**: Multimodal support
- **LLaVA (Open-source)**: Vision-language
- **GPT-4o**: Latest, fast vision model

### Text-Only (Still Powerful)
- **GPT-4**: Strong reasoning
- **Claude 3 Opus**: Long context, nuanced reasoning
- **Llama 2**: Open-source, offline capable
- **Mistral**: Fast, efficient
- **Qwen**: Multilingual support

## Cost-Benefit Analysis

| Model | Cost | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| GPT-4V | High | Medium | Excellent | Complex visual layouts |
| GPT-4 | Medium | Medium | Excellent | General extraction |
| Claude 3 Opus | Medium | Medium | Excellent | Long documents |
| Claude 3 Sonnet | Low | Fast | Good | Budget-conscious |
| Local Llama 2 | Zero | Slow | Okay | Offline, privacy |

## Advanced Techniques

### 1. Few-Shot Learning
Provide examples to improve accuracy:
```python
prompt = """
Examples:
HTML: <div class="price">$19.99</div>
Extract: $19.99

HTML: <span data-price="29.95">...</span>
Extract: $29.95

Now extract price from: {html}
"""
```

### 2. Chain-of-Thought Reasoning
Ask LLM to explain reasoning:
```python
prompt = """
Think step-by-step:
1. Identify the product container
2. Find the price element within it
3. Extract the numerical value
4. Return as JSON

HTML: {html}
"""
```

### 3. Output Validation
Use Pydantic for structured extraction:
```python
from pydantic import BaseModel

class Product(BaseModel):
    title: str
    price: float
    url: str

# LLM generates structured data matching schema
extraction = llm_call(
    html=html,
    schema=Product.model_json_schema()
)
product = Product(**extraction)
```

### 4. Embedding-Based Similarity
Find similar extraction patterns:
```python
# Cache embeddings of successful extractions
similar_patterns = find_similar_extractions(
    current_html,
    past_successes_embeddings
)
# Use similar patterns as examples
```

## Real-World Workflows

### Workflow 1: Article Extraction
```
1. User provides article URL
2. LLM extracts title, author, date, content
3. Format as structured data
4. Save to database
5. Log activity
```

### Workflow 2: E-commerce Monitoring
```
1. Periodic task triggered
2. Fetch product page
3. LLM extracts price, availability, reviews
4. Compare with previous data
5. Alert if price dropped or stock changed
6. Update analytics
```

### Workflow 3: Job Board Scraping
```
1. Search for jobs matching criteria
2. For each result, LLM extracts:
   - Title, company, location
   - Salary range
   - Required skills
   - Application URL
3. Deduplicate across sites
4. Score/rank by relevance
5. Send daily digest
```

## Error Handling

### Common LLM Extraction Errors
1. **Hallucination**: LLM invents data not in HTML
   - Solution: Include confidence scores, validate against original
2. **Incomplete extraction**: Missing some data
   - Solution: Multi-pass approach, ask for missing fields
3. **Format inconsistency**: Returns JSON sometimes, plain text others
   - Solution: Use structured outputs, Pydantic schemas
4. **Context length overflow**: HTML too long for model
   - Solution: Summarize HTML, extract relevant section, use longer context models

## Performance Optimization

### Speed
- Use faster models for simple tasks (Claude Haiku, Sonnet)
- Cache embeddings for similar pages
- Batch multiple extractions in single call
- Parallel API calls for multiple pages

### Cost
- Start with cheaper models, upgrade if needed
- Few-shot examples reduce error rates
- Reuse successful prompts
- Filter out irrelevant HTML before sending to LLM

## Limitations & When NOT to Use

### Don't Use LLM Extraction If:
- Data structure is simple (static HTML, clear selectors)
- Extreme scale (billions of pages) → Too expensive
- Real-time requirements → LLM calls too slow
- Privacy critical → Can't send data to external API
- Determinism required → LLMs non-deterministic

### Use LLM When:
- Layout frequently changes
- Complex reasoning needed
- Extraction logic is difficult to express in selectors
- Dealing with unstructured text
- Need adaptability across different sites
