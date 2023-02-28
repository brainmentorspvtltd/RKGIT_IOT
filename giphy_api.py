import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": "tom and jerry",
  "api_key": "1gPMgQWU9fDU9PPHW2Kr917sPJlo3n2g",
  "limit": "10"
})

with request.urlopen("".join((url, "?", params))) as response:
  data = json.loads(response.read())

