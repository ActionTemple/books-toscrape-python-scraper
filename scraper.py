import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import json
import os
from getch import getch

def menu():
    csv_mode = False
    clear_screen()
    print()
    while True:
        clear_screen()
        print("Scraper for books.toscrape.com")
        print("\n1: CSV\n2: JSON\n3: Exit")
        key_press = getch()
        if key_press == "1":
            csv_mode = True
            return csv_mode
        elif key_press == "2":
            csv_mode = False
            return csv_mode
        elif key_press == "3":
            clear_screen()
            print("\nGOODBYE")
            exit()
        
        
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def fetch_page(url):
    
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
    
def parse_books(soup):
    
    books = soup.find_all("article", class_="product_pod")
    return books

def find_next_page(soup):
    next_page = soup.find("li", class_="next")
    return next_page

def init_csv():
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability'])   

def write_csv(csv_list):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)

def build_dictionary(title, price, availability):
    
    book_dict = {"title": title,
                "price": price,
                "availability": availability}
    
    return book_dict

def write_JSON(books_list):
    with open("books.json", "w", encoding = "utf-8") as file:
        json.dump(books_list, file, indent=4, ensure_ascii=False)

def main():
    while True:
        csv_mode = menu()
        end = False
        url = "http://books.toscrape.com/"
        page = 1
        books_list = []
        csv_list = []
        if csv_mode:
            init_csv()
        
        while not end:     
            soup = fetch_page(url)
            books = parse_books(soup)
            
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", "price_color").get_text()
                availability = book.find("p", "instock availability").get_text("|", strip=True)
                if csv_mode:
                    csv_row = [title, price, availability]
                    csv_list.append(csv_row)
                else:
                    books_list.append(build_dictionary(title, price, availability))
                    
                
            next_page = find_next_page(soup)

            if not next_page:
                end = True
                if csv_mode:
                    write_csv(csv_list)
                else:
                    write_JSON(books_list)    
                clear_screen()
                print("FINISHED")
                
                while True:
                    print ("Press any key for menu:")
                    getch()
                    break
            else:     
                clear_screen()
                print(f"PAGE {page}")
                page += 1
                url = urljoin(url, (next_page.a.attrs["href"]))


if __name__ == "__main__":
    main()