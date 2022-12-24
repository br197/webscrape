from bs4 import BeautifulSoup
import re
import requests

search_term = input("What product you want to search for? ") #user input desired product

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"

page = requests.get(url).text #get page of url

doc = BeautifulSoup(page, "html.parser") # feed page into beautiful soup


items_found = {}

page_text = doc.find(class_="list-tool-pagination-text").strong #gets stuff in strong tag under this class
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1]) #get page numbers


#loop through pages

for page in range(1, pages+1): #dont want to start at 0 and go up to last page
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}" #loop for specific page
    page = requests.get(url).text #get page of url
    doc = BeautifulSoup(page, "html.parser") # feed page into beautiful soup
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell") #returns full item html

    items = div.find_all(text = re.compile(search_term)) #reg expression matches any text under div parent that contains any form of search term and which is the title of product
    for item in items:
        parent = item.parent #retrieves parent of item which is a href since title under that tag; sets parent as, a tagged href 
        if parent.name != "a": #checks if parent is a tag
            continue
        
        link = parent['href'] #grabs info from href attr of a tag, contains link to item
        next_parent = item.find_parent(class_="item-container") #looks for ancestor in tree that has a item container name
        try:
            price = next_parent.find(class_="price-current").find("strong").string #finds each price container info under item container and gets string in strong class
            items_found[item]= {"price": int(price.replace(",", "")), "link":link} #prints item name followed by price and link
        except:
            pass
    
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
 #sorted(iterable, key=key - function to execute to decide order, reverse = false(default/true)
 #1. convert items_found dictionary into list of tuples (key,value)
 #2. accesses value (dict) and call for value within dict of price key

for item in sorted_items:
    print(item[0]) #print name of item
    print(f"${item[1]['price']}") #f string of price
    print(item[1]['link']) #gets link
    print("-----------------------------------------")


    