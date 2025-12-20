# Rate Limiting

## Overview
Understanding and working within rate limit constraints.

## Rate Limiting Strategies
- Fixed window rate limiting
- Sliding window rate limiting
- Token bucket algorithm
- Leaky bucket algorithm

## Common Limits
- Requests per second
- Requests per minute
- Requests per hour
- Requests per day

## Response Codes
- 429 Too Many Requests
- 503 Service Unavailable
- 403 Forbidden

## Headers
- Retry-After
- X-RateLimit-Limit
- X-RateLimit-Remaining
- X-RateLimit-Reset

## Handling Rate Limits
- Implement exponential backoff
- Monitor rate limit headers
- Queue requests intelligently
- Use multiple IP addresses
- Distributed scraping
