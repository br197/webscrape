from bs4 import BeautifulSoup

#read "r" - read mode html file under name f

with open("/Users/briannaroundtree/Desktop/learning/web scraping/sample.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser") #parse file as html file under file name f

#print(doc.prettify())

#tag = doc.title
#tags = doc.find_all("p") #retrieves all p tags and what's inside

#tag.string = "hello"

#print(tag.string) #access string inside tag

#print(doc) #string title changed in document

#print(tags)

tags = doc.find_all("p")[0]

#print(tags.find_all("b")) # get all of b tags


