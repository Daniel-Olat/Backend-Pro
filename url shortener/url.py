import string
import random
import json
import os
from urllib.parse import urlparse

# Simple persistent mapping (file-based) so shortened URLs survive restarts
DATA_FILE = os.path.join(os.path.dirname(__file__), 'url_map.json')

def _load_map():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def _save_map(m):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=2)

url_map = _load_map()


def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    # ensure code is unique
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        if code not in url_map:
            return code


def shorten_url(long_url):
    # Basic validation: ensure URL has a scheme
    parsed = urlparse(long_url)
    if not parsed.scheme:
        long_url = 'http://' + long_url

    code = generate_code()
    url_map[code] = long_url
    _save_map(url_map)
    # For local testing, return localhost short URL on port 8000 (server.py)
    return f"http://127.0.0.1:8000/{code}"


def resolve_url(code):
    # Reload map from disk to ensure the server sees mappings created after it started
    m = _load_map()
    return m.get(code)


if __name__ == "__main__":
    # Example usage when run as a script
    long_url = "https://www.bing.com/search?q=stack+overflow"
    short_url = shorten_url(long_url)
    print("Shortened URL:", short_url)

    code = short_url.split("/")[-1]
    resolved_url = resolve_url(code)
    print("Resolved URL:", resolved_url)