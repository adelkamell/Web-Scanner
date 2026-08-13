# a mini web vulnerability scanner 
# V1 --> GET-based XSS


import requests
import sys

if len(sys.argv) < 2:
    print("Usage: python webscan.py <url>")
    sys.exit(1)

url = sys.argv[1]
payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]
for p in payloads:
    r = requests.get(url + "?q=" + p)
    if p in r.text:
        print(f"[!] XSS found with payload: {p}")