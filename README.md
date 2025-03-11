# 🪄 Favicon Spellcaster

A simple Python tool to calculate the **Shodan favicon hash** of any `favicon.ico` URL and generate the corresponding **Shodan DORK** to help you discover related infrastructure using the same icon.

## ✨ What it does

- Downloads a favicon from a given URL
- Encodes it in base64
- Calculates its [mmh3 hash](https://shodan.io/search/filters/http.favicon.hash) (the one used by Shodan)
- Outputs the Shodan DORK ready to paste into [https://www.shodan.io](https://www.shodan.io)

Perfect for **reconnaissance, OSINT, bug bounty, or threat hunting**.

## 🧙‍♂️ Why it's useful

Sometimes organizations reuse the same favicon across multiple environments (prod, staging, dev, test, etc). With this tool, you can identify systems that share that favicon — even if they don’t have obvious subdomains.

## 🔧 Usage

```bash
python favicon_spellcaster.py -u https://example.com/favicon.ico
