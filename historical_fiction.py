from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

page = requests.get(url).text #retrieves page

doc = BeautifulSoup(page, "html.parser") #got html of page

#data

products = []
prices = []
links = []
books_fic = {}

#get number of pages pages

pages_text = doc.select_one("li.current").text.strip() #selects first instance of current li class

pages = int(pages_text[-1])

#cycle through pages

for page in range(1,pages+1):
    url = f'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-{page}.html' #retrieves each page
    page = requests.get(url).text
    doc  = BeautifulSoup(page, "html.parser")
    div = doc.find_all(class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for item in div:

        #get product
        product = item.find("img", src = True)
        product_name = str(product["alt"])
        products.append(product_name)

        #get link
        link = item.find("a", href = True)
        web_link = "http://books.toscrape.com/catalogue/"+link["href"].split("/")[-2]
        links.append(web_link)
        
        #get price
        price = item.find(class_ = "price_color").text[2:]
        prices.append(float(price))


    for i in range(len(prices)):
        books_fic[products[i]] = {"price": prices[i], "Links": links[i]}


#print(books_fic.items()) #returns tuple with key followed by value

sort_dict = sorted(books_fic.items(), key = lambda x: x[1]["price"])# access 1st elem of tuple and price key

product_order = []
price_order = []
link_order = []

for i in sort_dict:
    product_order.append(i[0])
    price_order.append("$" + str(i[1]["price"]))
    link_order.append(i[1]["Links"])


#make excel document of all hist fic books, ascending order price
#print(product_order)
#print(len(price_order))
data = {"Book Title": product_order, "Price": price_order, "Link": link_order} #match titles to column titles
    
df = pd.DataFrame(data, columns = ["Book Title", "Price", "Link"])

#print(df)
df.to_excel("Historical Fiction Catalog.xlsx")




        
    


       
        
       