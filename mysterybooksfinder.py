#imports soup, pandas, re, requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

#retrieves doc and puts into soup

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
page = requests.get(url).text #gets text from page

doc = BeautifulSoup(page, "html.parser")

#compartments for data

products = []
prices = []
links = []
books = {}

#get pages

page_text = doc.select_one("li.current")
pages = int(str(page_text.text.strip()[-1]))

for page in range (1,pages+1):
    url = f"http://books.toscrape.com/catalogue/category/books/mystery_3/page-{page}.html"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") #gets all classes (books)

    for item in div: #for each book
        link = item.find("a", href = True) # access the href under a tag
        web_link = "http://books.toscrape.com/catalogue/"+link["href"].split("/")[-2]
        title = item.find("a", title = True)
        price = item.find("p", class_ = "price_color").string #get rid of p tags
        products.append(str(title).split(">")[-3].split("=")[-1]) #split string to get title
        links.append(web_link)
        prices.append(price[1:].replace("£", "$"))
    
    for i in range(0,len(products)):
        books[products[i]] = {"Price": float(prices[i][1:]), "Link": web_link}

    #sort books by price
    sorted_dict = sorted(books.items(), key=lambda x: x[1]['Price'])

    #make excel document of all mystery books from lowest to greatest price
    
    d = pd.DataFrame(sorted_dict, columns = ["Books", "Prices, Links"])

    df.to_excel("Mysterious Books.xlsx")

    
    
    