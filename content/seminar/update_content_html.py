from bs4 import BeautifulSoup
import os
import pprint

with open('../seminar_list/content.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
pprint.pprint(soup.decode())