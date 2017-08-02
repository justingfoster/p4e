import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.carquest.com/stores'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('a', class_='c-directory-list-content-item-link')

for tag in tags:
    url2 = 'https://www.carquest.com/' + tag["href"]
    print(url2)
    html2 = urllib.request.urlopen(url2, context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')

    tags2 = soup2.find_all('a', class_='c-directory-list-content-item-link')
    #newurl = 'https://www.carquest.com/' +

    for tag2 in tags2:
        try:
            url3 = tag2["href"]
            urlcut = url3[2:]
            url4 = 'https://www.carquest.com' + urlcut
            html3 = urllib.request.urlopen(url4, context=ctx).read()
            soup3 = BeautifulSoup(html3, 'html.parser')

            text = soup3.find_all('script', "js-map-config")
            paragraphs = []

            for par in text:
                paragraphs.append(str(par))

            parag = str(paragraphs)

            loc = re.search('locs":(.+?)"nearbyLocs',parag).group(0)
            #locs = re.search('locs":([a-z0-9])"nearbyLocs', parag).group(0)

            lon = re.findall('"longitude":(.+?),', loc)
            lat = re.findall('"latitude":(.+?),', loc)

            coordinates = dict(zip(lon,lat))

            for x,y in coordinates.items():
                print(x,", ",y)

        except:
            pass
