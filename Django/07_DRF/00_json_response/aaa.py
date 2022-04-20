import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
pprint(type(response))
pprint(type(response.json()))

article_list = response.json()

for article in article_list:
    print(article.get('content'))