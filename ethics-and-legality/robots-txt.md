# Robots.txt

## Overview
Understanding and respecting robots.txt directives.

## Robots.txt Basics
- Location: /robots.txt at domain root
- Controls bot access
- Standard Robots Exclusion Protocol
- Voluntary compliance

## Syntax
- User-agent
- Disallow
- Allow
- Crawl-delay
- Request-rate

## Example Structure
```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/

User-agent: Googlebot
Crawl-delay: 0

User-agent: *
Crawl-delay: 2
```

## Best Practices
- Always check robots.txt
- Respect Disallow directives
- Honor Crawl-delay
- Identify your bot properly
- Follow site guidelines
