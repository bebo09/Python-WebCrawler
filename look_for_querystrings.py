import requests
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup

base_domain = "wwww.devdungeon.com"
response = requests.get("https://www.devdungeon.com/archive")

soup = BeautifulSoup(response.text)

for a in soup.find_all("a"):
    #print(a.get("href"))
    url = urlparse(a.get("href"))
    if url.query:
        print("Querystring found in url: %s" % str(url))
        print(url.netloc)
    # CHeck if URL stays within domain
        # 1) URL is relative, begind with a /
    if url.netloc == "" or url.netloc == base_domain:
        print("On-site url detected: %s" % str(url))
        # 2) URL has the same netloc
