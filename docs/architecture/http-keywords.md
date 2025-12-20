# 🌐 HTTP Keywords & Concepts

This section explains **core HTTP terms and behaviors** that are especially important for **web data extraction systems**.
Most scraping failures can be diagnosed by correctly understanding these concepts.

---

## 📌 Overview

HTTP defines **how clients and servers communicate**.
For web data extraction, HTTP is not just a transport layer — it is a **signal system** that tells you:

* Whether access is allowed
* Whether content has moved
* Whether you are being throttled
* Whether the server is healthy

Understanding HTTP keywords allows you to **debug scraping issues systematically**, rather than guessing.

---

## 🔑 Request Methods

### **GET**

* Retrieves data from the server
* Should not change server state
* Most commonly used method in scraping

**Scraping relevance**

* Used to fetch pages, listings, articles
* Safe to retry if failures occur

---

### **POST**

* Sends data to the server
* Often triggers server-side processing

**Scraping relevance**

* Submitting search forms
* Accessing internal APIs behind websites
* Pagination via form-based navigation

⚠️ POST requests are more sensitive to misuse and may trigger protections faster.

---

## 🧾 HTTP Headers

Headers provide **context** about the request and client.

### Common Headers in Scraping

* **User-Agent**

  * Identifies the client software
  * Missing or unrealistic values often trigger blocks

* **Accept**

  * Tells the server which response formats are acceptable
  * Helps receive HTML, JSON, or other formats correctly

* **Authorization**

  * Carries credentials or tokens
  * Required for authenticated endpoints (when legally permitted)

Headers strongly influence:

* Response content
* Rate limits
* Bot detection behavior

---

## 🔄 Request–Response Flow (Diagram)

```
Client (Scraper)
     |
     |  HTTP Request
     |  - Method (GET / POST)
     |  - Headers
     |  - Cookies
     v
Server
     |
     |  HTTP Response
     |  - Status Code
     |  - Headers
     |  - Body (HTML / JSON)
     v
Client (Parser & Storage)
```

Every scraping decision should be based on **what comes back in the response**, not assumptions.

---

## 📊 HTTP Status Codes (Scraping-Focused)

### ✅ **200 OK**

* Request succeeded
* Content returned normally

**Action**

* Parse and extract data

---

### 🔁 **301 / 302 Redirects**

* Resource has moved (permanently or temporarily)

**Scraping relevance**

* Follow redirects to reach canonical URLs
* Important for pagination and SEO-based routing

---

### 🚫 **403 Forbidden**

* Server understood the request but denied access

**Common causes**

* Missing headers
* IP-based blocking
* Bot detection triggers

**Action**

* Inspect headers and request behavior
* Do not retry aggressively

---

### 🕒 **429 Too Many Requests**

* Rate limit exceeded

**Scraping relevance**

* Clear signal to slow down

**Action**

* Implement delays
* Use exponential backoff
* Reduce request frequency

---

### ⚠️ **5xx Server Errors**

* Server-side failure

Examples:

* 500 Internal Server Error
* 502 Bad Gateway
* 503 Service Unavailable

**Action**

* Retry after delay
* Treat as temporary failure
* Avoid hammering the server

---

## 🧠 How Scrapers Should Interpret HTTP Signals

| Signal  | Meaning        | Recommended Action |
| ------- | -------------- | ------------------ |
| 200     | Success        | Extract data       |
| 301/302 | Redirect       | Follow safely      |
| 403     | Access blocked | Inspect request    |
| 429     | Rate limit     | Backoff & retry    |
| 5xx     | Server issue   | Retry with delay   |

HTTP responses are **feedback**, not just outcomes.

---

## 🚧 Common Mistakes in Scraping

* Treating all failures as parsing issues
* Ignoring status codes
* Retrying aggressively on 403 or 429
* Not following redirects
* Using unrealistic headers

Most scraping bugs are **HTTP-level problems**, not DOM problems.

---

## ⚖️ Ethical & Responsible Considerations

Correct interpretation of HTTP signals helps:

* Reduce unnecessary traffic
* Avoid accidental abuse
* Respect website infrastructure
* Build sustainable scraping systems

This repository focuses on **learning HTTP behavior**, not bypassing restrictions.

---

## 🔑 Key Takeaways

* HTTP keywords are diagnostic tools
* Status codes communicate intent and limits
* Headers shape server responses
* Good scrapers listen to HTTP signals
* Understanding HTTP prevents most failures

---

