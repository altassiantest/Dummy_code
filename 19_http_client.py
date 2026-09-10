import urllib.request
import json

def fetch_json(url, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read().decode())

def fetch_text(url, timeout=10):
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return resp.read().decode()

if __name__ == '__main__':
    try:
        data = fetch_json('https://api.github.com')
        print('Keys:', list(data.keys())[:5])
    except Exception as e:
        print('Error:', e)
