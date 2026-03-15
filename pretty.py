import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"
#print(f"encoding = {response.encoding}, apparent_encoding = {response.apparent_encoding}")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find("li", class_="next"))

   
#print(soup.prettify())
    