import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://stores.advanceautoparts.com/index.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Find all state URLs
tags = soup.find_all('a', class_='c-directory-list-content-item-link')

for tag in tags:
    url2 = 'https://stores.advanceautoparts.com/' + tag["href"]
    html2 = urllib.request.urlopen(url2, context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')

    tags2 = soup2.find_all('a', class_='c-directory-list-content-item-link')

    for tag2 in tags2:
        try:
            url3 = 'https://stores.advanceautoparts.com/' + tag2["href"]
            html3 = urllib.request.urlopen(url3, context=ctx).read()
            soup3 = BeautifulSoup(html3, 'html.parser')
            print(url3)

            #text = soup3.find_all('script', "js-map-config")
            for text in soup3.stripped_strings:
                text2 = repr(text)
                try:
                    lon = re.search('"longitude":(.+?),', text).group(1)
                    lat = re.search('"latitude":(.+?),', text).group(1)
                    print("longitude: ", lon)
                    print("latitude: ", lat)
                except:
                    pass

        except:
            pass
