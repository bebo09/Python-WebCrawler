import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class DomainCrawler:

    def __init__(self, starting_url):
        self.starting_url = starting_url
        self.parsed_starting_url = urlparse(starting_url)
        self.visited_urls = []
        self.active_processors = 0

    def process_page(self, href):
        url = urlparse(href)
        if url.netloc == "":
            href = self.parsed_starting_url.scheme + "://" + \
                   self.parsed_starting_url.netloc + \
                   href

        if href not in self.visited_urls:
            self.visited_urls.append(href)
        else:
            return

        print("[*] Processing %s % href")

        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        for a in soup.find_all("a"):
            if self.does_url_stay_onsite(a.get("href")):
                self.process_page(a.get("href"))

    def does_url_stay_onsite(self, href):
        url = urlparse(href)
        if url.netloc == "" or url.netloc == self.parsed_starting_url.netloc:
            return True

    def start(self):
        self.process_page(self.starting_url)
        print("[+] Complete!")


if __name__ == " __main__":
    crawler = DomainCrawler('https://www.google.com')
    crawler.start()
