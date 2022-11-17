import requests

URL = "https:// Enter URL Here"
page = requests.get(URL)

print(page.text) 
