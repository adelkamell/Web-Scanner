# Mini Web Vulnerability Scanner

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-orange.svg)]()

A lightweight command-line web vulnerability scanner for detecting XSS vulnerabilities through GET parameters and HTML form injection.

## 🚀 Features

- **Form-based XSS Detection**: Automatically finds HTML forms and injects payloads into all input fields
- **GET-based XSS Detection**: Scans URL parameters for common XSS payloads
- **Multi-method Support**: Handles both GET and POST form submissions
- **Automated Form Parsing**: Uses BeautifulSoup to extract and analyze HTML forms
- **Lightweight & Fast**: Minimal dependencies for quick scanning

## 📋 Prerequisites

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mini-web-scanner.git
cd mini-web-scanner
```

### Install dependencies:

```bash
pip install requests beautifulsoup4
```

## 💻 Usage
Basic Usage
```bash
python webscan.py <target_url>
```

### Examples
```bash
# Scan a search page
python webscan.py https://example.com/search

# Scan a contact form
python webscan.py https://example.com/contact

# Scan any page with forms
python webscan.py https://example.com
```

### How It Works
Form Discovery: Parses HTML to find all forms

Payload Injection: Injects test payloads into every input field

Form Submission: Automatically submits forms (GET/POST)

Vulnerability Detection: Checks responses for reflected payloads

### Output Example
```text
[!] XSS in https://example.com/search (action=/search.php)
[!] XSS in https://example.com/contact (action=/submit.php)
[!] XSS found with payload: <script>alert(1)</script>
```

### 🛡️ Payloads Tested
Current Payloads
- <script>alert('XSS')</script> - JavaScript injection

- <script>alert(1)</script> - Basic script injection

- <img src=x onerror=alert(1)> - Image-based XSS

### Supported Form Types
- GET Forms: URL parameter injection

- POST Forms: Data submission injection

- Multi-input Forms: All fields tested simultaneously

### ⚠️ Disclaimer
This tool is for educational and authorized testing purposes only.

Only use on websites you own or have explicit permission to test

Unauthorized scanning may be illegal

The developers assume no liability for misuse

Always obtain written permission before scanning

### 🔒 Security Best Practices
Always obtain written permission before scanning

Test in isolated environments when possible

Use responsibly and ethically

Document all testing activities

Report vulnerabilities responsibly

### 🚧 Current Limitations
Limited payload set

No WAF bypass or advanced evasion techniques

No crawling capabilities (manual URL entry only)

No authentication/session support

Single-threaded scanning

No report generation

### 📈 Future Enhancements
□ Custom payload lists
□ Advanced XSS evasion techniques
□ DOM-based XSS detection
□ Multi-threaded scanning
□ SQL injection detection
□ Command injection detection
□ Report generation (HTML/JSON)
□ Authentication support (cookies/sessions)
□ Crawling capabilities
□ API endpoint scanning

### 🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


🙏 Acknowledgments
BeautifulSoup - For HTML parsing capabilities

Requests - For HTTP handling

OWASP - For XSS documentation and guidelines

The security community for payload suggestions

### Version History

v2.0: Added form detection, BeautifulSoup integration, POST support

v1.0: Basic GET-based XSS detection

**Made with ❤️ for the security community**