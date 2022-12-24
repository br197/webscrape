from bs4 import BeautifulSoup

import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url) #getting content of newegg page

#print(result.text) #store result in text file

doc = BeautifulSoup(result.text, "html.parser")

#print(doc.prettify())

prices = doc.find_all(text = "$") #look for text with dollar sign

#print(prices) # dollar signs allow us to access price, dollar sign parent is p tag

parent = prices[0].parent

strong = parent.find("strong")

print(strong.string)