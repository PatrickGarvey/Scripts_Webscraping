import os
import requests
from bs4 import BeautifulSoup


import sys
sys.path.append('../')

from robots import parse_robots_txt

### TODOs
# parse robots
# create sitemap (crawl site)
# scrape sites

def scrape_wiki():
    print("--- start scraping ---")
    URL = "https://www.el-wiki.net"
    parse_robots_txt(URL)





if __name__ == "__main__":
    scrape_wiki()
