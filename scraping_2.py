import urllib.request as url
import bs4

product = input("Enter product name : ")
product = product.replace(" ", "+").lower()
for k in range(1,6):
    path = f"https://www.flipkart.com/search?q={product}&page={k}"

    response = url.urlopen(path)   # making HTTPRequest
    page = bs4.BeautifulSoup(response, "lxml")
    titleList = page.find_all('div', {'class' : '_4rR01T'})
    priceList = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})
    for i in range(len(titleList)):
        print(titleList[i].text)
        print(priceList[i].text)
        print("*" * 30)

