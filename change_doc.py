from bs4 import BeautifulSoup

import re

with open("/Users/briannaroundtree/Desktop/learning/web scraping/sample2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type = "text") #find input tags with text type

for tag in tags:
    tag['placeholder'] = "I changed you!" #modify attribute placeholder

#create new file with change
with open("/Users/briannaroundtree/Desktop/learning/web scraping/change.html", "w") as file:
    file.write(str(doc))