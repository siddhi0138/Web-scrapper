# 🤖 robots.txt

## 📌 Overview

`robots.txt` is a **standardized mechanism** that websites use to communicate **crawl preferences and access rules** to automated agents such as search engines and scrapers.

While `robots.txt` is **not a security mechanism**, it plays a critical role in:

* Ethical web data extraction
* Reducing server load
* Preventing accidental scraping of sensitive areas

Responsible scraping systems treat `robots.txt` as a **first-class signal**, not an afterthought.

---

## 📍 robots.txt Basics

* **Location**: Always at the root of a domain (`/robots.txt`)
* **Scope**: Applies per host (subdomains have separate files)
* **Purpose**: Express crawl rules and preferences
* **Protocol**: Robots Exclusion Protocol (REP)
* **Compliance**: Voluntary but strongly recommended

Ignoring `robots.txt` may not be illegal by itself, but it significantly increases ethical and operational risk.

---

## 🧠 What robots.txt Controls (and What It Doesn’t)

### ✅ Controls

* Which paths bots should or should not crawl
* Crawl pacing recommendations
* Bot-specific rules

### ❌ Does NOT Control

* Authentication or authorization
* Access to private data
* Content indexing guarantees
* Security enforcement

`robots.txt` communicates **intent**, not protection.

---

## 🧾 Syntax & Directives

### 🔹 `User-agent`

Specifies which crawler the rules apply to.

* `*` applies to all bots
* Specific names apply to individual crawlers

---

### 🔹 `Disallow`

Indicates paths that should not be crawled.

Example:

```
Disallow: /admin/
```

---

### 🔹 `Allow`

Overrides disallow rules for specific paths.

Example:

```
Allow: /public/
```

---

### 🔹 `Crawl-delay`

Suggests delay (in seconds) between requests.

Example:

```
Crawl-delay: 2
```

---

### 🔹 `Request-rate`

Specifies request limits over time (less widely supported).

Example:

```
Request-rate: 10/1m
```

Support for directives may vary across bots.

---

## 📄 Example robots.txt

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

Interpretation:

* All bots must avoid `/admin/` and `/private/`
* `/public/` is explicitly allowed
* Default crawl delay is 2 seconds
* Googlebot has a special rule

---

## 🔄 robots.txt Evaluation Flow

```
Scraper Starts
      │
      ▼
Fetch /robots.txt
      │
      ▼
Parse User-agent Rules
      │
      ▼
Is Target Path Allowed?
   ├─ No → Do Not Crawl
   └─ Yes
        │
        ▼
Apply Crawl-delay
        │
        ▼
Send Request
```

This flow should occur **before any scraping begins**.

---

## 🛠 robots.txt in Scraping Systems

Scraping systems should:

* Cache robots.txt per domain
* Re-fetch periodically (rules may change)
* Apply rules per User-Agent
* Respect the most restrictive matching rule

robots.txt parsing is a **core infrastructure feature**, not optional logic.

---

## 🚧 Common Mistakes

* Ignoring robots.txt entirely
* Assuming all directives are optional
* Using wildcard User-Agents irresponsibly
* Forgetting crawl-delay enforcement
* Applying rules incorrectly across subdomains

---

## ⚖️ Ethical & Practical Considerations

Respecting robots.txt:

* Signals good-faith behavior
* Reduces blocking and throttling
* Protects site stability
* Improves scraper longevity

Most reputable organizations **require robots.txt compliance**.

---

## ✅ Best Practices

* Always fetch robots.txt first
* Honor all `Disallow` rules
* Enforce crawl delays consistently
* Identify your bot with a clear User-Agent
* Log robots.txt decisions
* Stop scraping if rules change unexpectedly

---

## 🔑 Key Takeaways

* robots.txt expresses crawl preferences
* It is voluntary but ethically binding
* It does not secure content
* Ignoring it increases risk
* Responsible scrapers treat it as mandatory

---
