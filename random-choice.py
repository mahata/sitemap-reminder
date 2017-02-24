#!/usr/bin/env python3

import urllib.request
import random

import bs4

url = "https://mahata.wordpress.com/sitemap.xml"
xml = urllib.request.urlopen(url).read().decode("utf-8")

soup = bs4.BeautifulSoup(xml, "lxml")
locs = [loc.text for loc in soup.findAll("loc")]

article_url = locs[random.randint(0, len(locs) - 1)]

print(article_url)
