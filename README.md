# Proxy Rotation and Web Scraping Automation

This project implements a Python-based tool for testing the effectiveness of free proxies and rotating proxies for web scraping. The tool is designed to automate the process of scraping web pages and validating proxy reliability, ensuring anonymity and bypassing restrictions.

## Features

- **Proxy Rotation:** Implements a proxy rotation mechanism using a list of free proxies, ensuring anonymity and avoiding IP blocking during web scraping.
- **Web Scraping Automation:** Automates the scraping of multiple web pages from the "Books to Scrape" website, testing the reliability and performance of each proxy.
- **Proxy Validation:** Validates proxies by testing their connectivity to a public API and checking their response status codes to ensure that they are working.
- **Error Handling and Timeouts:** Includes error handling with retries and timeouts to deal with unreliable proxies, ensuring robustness during the scraping process.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/proxy-rotation-web-scraping.git
   run python main.py
