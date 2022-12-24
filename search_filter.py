from bs4 import BeautifulSoup

import re #import regular expression capability

with open("/Users/briannaroundtree/Desktop/learning/web scraping/sample2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#-----class names -----
#tags = doc.find_all(class_= "btn-item") #search for class name#

tags = doc.find_all(text=re.compile("\$.*"), limit = 1) #look for anything including and after dollar sign, limit to n results
for tag in tags:
    print(tag.strip()) #strip white space from tag re



#result = doc.find("option")

#print(result)



#-----modify attributes of a tag ie value = ------

#tags = doc.find_all(["p", "div", "li"]) #find stuff in multiple tags

#tags = doc.find_all(["option"], text = "Undergraduate",  value = "undergraduate") #search for option tag with undergraduate text
#print(tags)

#tag['selected'] = 'false' #change attribute like using a dictionary

#tag['color'] = "blue" #add attribute


#------see all attributes:-----

#print(tag.attrs)

#print(tag)