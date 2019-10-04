import requests
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup

starting_url = "https://www.devdungeon.com/archive"

parsed_starting_url = urlparse(starting_url)
response = requests.get(starting_url)
soup = BeautifulSoup(response.text)
for a in soup.find_all("a"):
    #print(a.get("href"))
    url = urlparse(a.get("href"))
    if url.query:
        print("Querystring found in url: %s" % str(url))
        print(url.netloc)
    # CHeck if URL stays within domain
        # 1) URL is relative, begind with a /
    if url.netloc == "" or url.netloc == parsed_starting_url.netloc:
        print("On-site url detected: %s" % str(url))
        # 2) URL has the same netloc
