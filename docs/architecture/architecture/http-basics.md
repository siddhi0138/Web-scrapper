# 🌐 HTTP Basics

## 📌 Overview

The **Hypertext Transfer Protocol (HTTP)** is the foundational communication protocol of the web.
Every web data extraction system — from simple scripts to large-scale crawlers — relies on HTTP to request, receive, and interpret web content.

Understanding HTTP deeply is critical because **scraping failures are often HTTP misunderstandings**, not parsing problems.

---

## 🧠 Why HTTP Matters for Web Data Extraction

Web data extraction is fundamentally about **correctly interacting with HTTP servers**.

A scraper must:

* Send valid requests
* Interpret responses accurately
* Handle failures gracefully
* Mimic legitimate client behavior

Most scraping issues arise from:

* Incorrect headers
* Misused HTTP methods
* Misinterpreted status codes
* Broken request lifecycles

---

## 🔑 Key Concepts

### 1️⃣ HTTP Methods

HTTP methods define **what action the client wants the server to perform**.

Commonly used methods in scraping:

* `GET` — Retrieve resources
* `POST` — Submit data or trigger server-side processing
* `PUT` — Update existing resources
* `DELETE` — Remove resources

Choosing the wrong method can lead to:

* Access denial
* Unexpected server responses
* Triggered security mechanisms

---

### 2️⃣ Status Codes

HTTP status codes communicate the **result of a request**.

They are grouped by category:

* **2xx** — Success
* **3xx** — Redirection
* **4xx** — Client-side errors
* **5xx** — Server-side errors

Scrapers must **react programmatically** to status codes rather than assuming success.

---

### 3️⃣ Headers and Metadata

HTTP headers carry **contextual information** about requests and responses.

They influence:

* Content negotiation
* Authentication
* Caching behavior
* Rate limiting
* Bot detection

Incorrect or missing headers are a common cause of scraping blocks.

---

### 4️⃣ Request / Response Lifecycle

Every HTTP interaction follows a structured flow:

1. Client constructs a request
2. Request is sent to the server
3. Server processes the request
4. Server returns a response
5. Client interprets status, headers, and body

Understanding this lifecycle helps diagnose:

* Slow responses
* Unexpected redirects
* Incomplete data
* Intermittent failures

---

## 📥 HTTP Methods Explained

### **GET**

* Retrieves data from the server
* Should not modify server state
* Most commonly used in scraping

Used for:

* Articles
* Listings
* Public datasets

---

### **POST**

* Sends data to the server
* Often used by forms and APIs
* May trigger server-side logic

Relevant when:

* Submitting search forms
* Triggering dynamic queries
* Interacting with hidden endpoints

---

### **PUT**

* Updates existing server resources
* Rarely used in scraping
* Common in RESTful APIs

---

### **DELETE**

* Removes server resources
* Typically restricted
* Almost never used in scraping contexts

---

## 📊 Common HTTP Status Codes

### Successful Responses

* **200 OK** — Request successful
* **201 Created** — Resource created
* **204 No Content** — Success without response body

---

### Redirection Responses

* **301 Moved Permanently** — URL changed permanently
* **302 Found** — Temporary redirect
* **307 Temporary Redirect** — Method-preserving redirect

Redirect handling is important for:

* Canonical URLs
* Tracking final destinations
* Avoiding infinite loops

---

### Client Errors

* **400 Bad Request** — Invalid request format
* **401 Unauthorized** — Authentication required
* **403 Forbidden** — Access denied
* **404 Not Found** — Resource missing
* **429 Too Many Requests** — Rate limiting

Status `429` is especially important for scrapers and often signals throttling.

---

### Server Errors

* **500 Internal Server Error**
* **502 Bad Gateway**
* **503 Service Unavailable**
* **504 Gateway Timeout**

Server errors are usually **temporary** and should trigger retries with backoff.

---

## 🛠 HTTP Headers in Scraping Context

Important headers include:

* `User-Agent` — Identifies the client
* `Accept` — Specifies expected response format
* `Accept-Language` — Language preferences
* `Referer` — Navigation context
* `Cookie` — Session and state handling

Headers influence whether a request is:

* Treated as legitimate
* Rate-limited
* Served alternate content

---

## 🚧 Common HTTP Pitfalls in Scraping

* Assuming every response is `200 OK`
* Ignoring redirects
* Hardcoding URLs without following canonical links
* Sending unrealistic or missing headers
* Retrying aggressively without delay

Robust scraping systems treat HTTP responses as **signals**, not just data carriers.

---

## ⚖️ Ethical and Responsible Usage

Correct HTTP usage helps:

* Reduce server load
* Avoid accidental abuse
* Respect website policies
* Build sustainable data pipelines

This repository emphasizes **understanding HTTP behavior**, not exploiting it.

---

## 🔑 Key Takeaways

* HTTP is the backbone of web data extraction
* Methods define intent; status codes define outcome
* Headers shape server behavior
* Most scraping bugs are HTTP-level issues
* Good HTTP handling leads to reliable systems

---

