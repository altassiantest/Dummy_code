import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.url_map[short] = url
        return short

    def expand(self, short):
        return self.url_map.get(short)

if __name__ == '__main__':
    s = URLShortener()
    short = s.shorten('https://example.com/very/long/url')
    print('Short:', short)
    print('Expanded:', s.expand(short))
