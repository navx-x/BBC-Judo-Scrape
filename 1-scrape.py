# Naveed - Scrape to pull content from BBC Judo site.
# 16:31 02/01/2018
# Yusuf

from selenium import webdriver
from bs4 import BeautifulSoup
import io



url = 'http://www.bbc.co.uk/sport/judo'

browser = webdriver.Firefox()

browser.get(url)

def get_html_data():
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    filename = str('bbc-judo') + '.html'

    with io.open(filename, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(str(url) + '  Done')
    print()
    print(str(filename) + ' saved locally')


get_html_data()

browser.close()
