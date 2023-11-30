import requests
import webbrowser
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true;"
response = requests.request(method="GET", url=url)


pprint(response.json()[0]['coatOfArms']['png'])
url=(response.json()[0]['coatOfArms']['png'])


webbrowser.open(url)