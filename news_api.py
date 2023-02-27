import urllib.request as url
import json
path = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=695e07af402f4b119f0703e9b19f4683"
response = url.urlopen(path)
data = json.load(response)
articles = data['articles']

for i in range(len(articles)):
    print(articles[i]['title'])
    print("*" * 40)
