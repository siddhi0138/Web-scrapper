# Anti-Bot Evasion for Agents

## Understanding Bot Detection

Websites implement multiple layers of detection:

1. **Behavioral Analysis**: Request patterns, timing, frequency
2. **Device Fingerprinting**: Browser characteristics, hardware info
3. **Headless Detection**: Checking for automation frameworks
4. **Browser Capabilities**: Missing or unusual features
5. **User-Agent Analysis**: Known bot signatures
6. **Network Patterns**: Multiple requests from same IP
7. **Content Patterns**: Identical request sequences
8. **JavaScript Execution**: Validation code in runtime

## Agent-Specific Challenges

### Challenge 1: Speed
- Agents operate too fast compared to humans
- Solution: Add random delays between actions

### Challenge 2: Consistency
- Agents repeat identical patterns
- Solution: Introduce variability (random mouse movements, scroll timing)

### Challenge 3: Incomplete Browser
- Headless browsers missing features
- Solution: Use headed browsers, stealth plugins

### Challenge 4: Network Fingerprinting
- All requests from same IP
- Solution: Proxy rotation, distributed agents

## Evasion Strategies for Agents

### Strategy 1: Realistic User Agents
```python
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
]
random_agent = random.choice(user_agents)
```

### Strategy 2: Browser Stealth
```python
# Puppeteer stealth plugin
import stealth from 'puppeteer-extra-plugin-stealth'
puppeteer.use(stealth())

# Playwright with stealth settings
context = await browser.new_context(
    viewport={'width': 1920, 'height': 1080},
    user_agent='Mozilla/5.0...',
    locale='en-US',
    timezone_id='America/New_York'
)
```

### Strategy 3: Human-Like Interaction
```python
async def human_like_click(page, selector):
    # Move mouse smoothly
    element = await page.query_selector(selector)
    box = await element.bounding_box()
    
    # Add random offset
    x = box['x'] + random.uniform(0, box['width'])
    y = box['y'] + random.uniform(0, box['height'])
    
    # Move with random speed
    await page.mouse.move(x, y, steps=random.randint(5, 15))
    await page.mouse.click()
```

### Strategy 4: Variable Timing
```python
import random
import asyncio

async def random_delay():
    """Human-like random delay"""
    # 90% of time: 0.5-3 seconds
    # 10% of time: 5-15 seconds (thinking hard)
    if random.random() < 0.9:
        await asyncio.sleep(random.uniform(0.5, 3))
    else:
        await asyncio.sleep(random.uniform(5, 15))
```

### Strategy 5: Proxy Rotation
```python
class ProxyRotator:
    def __init__(self, proxy_list):
        self.proxies = proxy_list
        self.current = 0
    
    def get_next_proxy(self):
        proxy = self.proxies[self.current]
        self.current = (self.current + 1) % len(self.proxies)
        return proxy
    
    async def make_request(self, url):
        proxy = self.get_next_proxy()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, proxy=proxy) as resp:
                return await resp.text()
```

### Strategy 6: Browser Fingerprinting
```python
# Randomize fingerprint characteristics
context = await browser.new_context(
    color_scheme='dark' if random.random() > 0.5 else 'light',
    locale=random.choice(['en-US', 'en-GB', 'de-DE']),
    timezone_id=random.choice([
        'America/New_York',
        'Europe/London',
        'America/Los_Angeles'
    ]),
    screen={'width': 1920, 'height': 1080},
    device_scale_factor=random.choice([1, 1.25, 1.5])
)
```

### Strategy 7: Request Headers
```python
def get_realistic_headers():
    return {
        'User-Agent': random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/',
    }
```

### Strategy 8: Cookies & Sessions
```python
# Persist cookies across sessions
context_options = {
    'storage_state': 'session_state.json',
}
context = await browser.new_context(**context_options)

# Maintain realistic cookie lifecycle
await page.context.add_cookies([
    {
                'name': 'session_id',
                'value': generate_session_id(),
                'domain': 'example.com',
                'path': '/',
                'expires': int(time.time()) + 3600
            }
])
```

### Strategy 9: JavaScript Execution
```python
# Execute legitimate JavaScript
await page.evaluate("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false
    });
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3]
    });
""")
```

### Strategy 10: Distributed Agents
```python
# Multiple agents with different characteristics
agents = [
    Agent(proxy=proxy1, user_agent=ua1, location='US'),
    Agent(proxy=proxy2, user_agent=ua2, location='UK'),
    Agent(proxy=proxy3, user_agent=ua3, location='DE'),
]

# Distribute work across agents
for url in urls:
    agent = random.choice(agents)
    agent.scrape(url)
```

## CAPTCHA Handling

### Strategy 1: Avoid Triggering
- Respect rate limits
- Human-like behavior
- Proper delays

### Strategy 2: CAPTCHA Solving Services
```python
from selenium import webdriver
from anticaptchaofficial.recaptchav2proxyless import *

def solve_captcha(page_url):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_website_key("6LcXMEUUAAAAAK...") # From page
    solver.set_website_url(page_url)
    
    g_response = solver.solve_and_return_solution()
    if g_response:
        return g_response  # Use in form submission
    return None
```

### Strategy 3: Browser Automation CAPTCHA
```python
# For image CAPTCHAs - save and solve manually
await page.screenshot(path='captcha.png')
# Manual input required
captcha_answer = input("Solve CAPTCHA: ")
```

## Testing Evasion

### Check Bot Detection
```python
async def test_detection(page):
    # Check for navigator.webdriver
    is_webdriver = await page.evaluate('() => navigator.webdriver')
    
    # Check for chrome property
    has_chrome = await page.evaluate('() => !!window.chrome')
    
    # Check for plugins
    plugins_length = await page.evaluate('() => navigator.plugins.length')
    
    return {
        'webdriver_detected': is_webdriver,
        'chrome_property': has_chrome,
        'plugins': plugins_length
    }
```

## Rate Limiting Compliance

### Respect robots.txt
```python
import requests
from urllib.robotparser import RobotFileParser

def can_fetch(url):
    rp = RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp.can_fetch('*', url)
```

### Implement Backoff
```python
async def request_with_backoff(url, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = await fetch(url)
            if response.status == 429:  # Too Many Requests
                wait = 2 ** attempt
                await asyncio.sleep(wait)
                continue
            return response
        except Exception as e:
            wait = 2 ** attempt
            await asyncio.sleep(wait)
```

## Ethical Considerations

### Do's
- ✓ Check robots.txt
- ✓ Respect rate limits
- ✓ Use public data
- ✓ Transparent logging
- ✓ Identify yourself

### Don'ts
- ✗ Bypass CAPTCHA unethically
- ✗ Steal proprietary data
- ✗ Violate Terms of Service
- ✗ DDoS through aggressive scraping
- ✗ Harvest personal information

## Red Flags That Trigger Detection

| Behavior | Problem | Solution |
|----------|---------|----------|
| Perfect timing | Too human-like | Add randomness |
| All requests identical | Automated pattern | Vary requests |
| Rapid requests | Too fast | Add delays |
| No referrer | Missing context | Set referrer headers |
| Old user agent | Outdated browser | Update user agent pool |
| Same IP always | Obvious bot | Rotate proxies |
| No cookies | Stateless | Maintain sessions |
| No headers | Minimal requests | Add realistic headers |
