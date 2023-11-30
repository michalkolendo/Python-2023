import requests
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"
response = requests.request(method="GET", url=url)

pprint(response.json())

print()
print(25*"*")
print()
print(response.json()['value'])




import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true;"
response = requests.request(method="GET", url=url)

pprint(response.json())

print()
print(25*"*")
print()
print(response.json()['value'])