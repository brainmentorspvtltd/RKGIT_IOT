import urllib.request as url
import bs4
path = "https://www.flipkart.com/search?q=iphone+13"

response = url.urlopen(path)   # making HTTPRequest
page = bs4.BeautifulSoup(response, "lxml")
title = page.find('div', {'class' : '_4rR01T'})
print(title.text)

