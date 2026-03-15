import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

end = False
url = "http://books.toscrape.com/"
while not end:
    response = requests.get(url)
    response.encoding = "utf-8"
    #print(f"encoding = {response.encoding}, apparent_encoding = {response.apparent_encoding}")
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", "price_color").get_text()
        availability = book.find("p", "instock availability").get_text("|", strip=True)
    
        #print(book.prettify())
        print(title, price, availability)

    #print(soup.find("li", class_="next").prettify())
    next_page = soup.find("li", class_="next")
    #if next_page == None:
     #   end = True

    #print (next_page.a.attrs["href"])

    #print(urljoin(url, (next_page.a.attrs["href"])))
    if not next_page:
        end = True
    else:    
        url = urljoin(url, (next_page.a.attrs["href"]))
    






