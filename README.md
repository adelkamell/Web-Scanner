# Mini Web Vulnerability Scanner

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A lightweight command-line web vulnerability scanner focused on detecting GET-based Cross-Site Scripting (XSS) vulnerabilities.

## 🚀 Features

- **GET-based XSS Detection**: Scans for common XSS payloads in URL parameters
- **Lightweight & Fast**: Minimal dependencies for quick scanning
- **Command-line Interface**: Easy to use with simple syntax
- **Payload Testing**: Includes common XSS vectors for comprehensive testing

## 📋 Prerequisites

- Python 3.x
- `requests` library

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mini-web-scanner.git
cd mini-web-scanner
```

### Install required dependencies:

```bash
pip install requests
```

## 💻 Usage
### Basic usage:

``` bash
python webscan.py <target_url>
```

### Examples
Scan a website for XSS vulnerabilities:

```bash
python webscan.py https://example.com/search
```

### The scanner will automatically test the URL with multiple XSS payloads and report any findings.

### Output Example
```text
[!] XSS found with payload: <script>alert(1)</script>
[!] XSS found with payload: <img src=x onerror=alert(1)>
```

### 🛡️ Payloads Tested
The scanner currently tests for the following XSS vectors:

- <script>alert(1)</script> - Basic script injection

- <img src=x onerror=alert(1)> - Image-based XSS

### ⚠️ Disclaimer
This tool is for educational and authorized testing purposes only.

Only use on websites you own or have explicit permission to test

Unauthorized scanning may be illegal

The developers assume no liability for misuse

### 🔒 Security Best Practices
Always obtain written permission before scanning

Test in isolated environments when possible

Use responsibly and ethically

Document all testing activities

### 🚧 Limitations
Version 1: Only supports GET-based XSS detection

Limited payload set (can be extended)

No support for POST requests

No advanced evasion techniques

No report generation features

### 📈 Future Enhancements
□ Support for POST-based XSS
□ Custom payload lists
□ Advanced evasion techniques
□ Report generation
□ Multi-threaded scanning
□ SQL injection detection
□ Command injection detection

### 🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

🙏 Acknowledgments
OWASP for XSS documentation and testing guidelines

The security community for payload suggestions

### Made with ❤️ for the security community