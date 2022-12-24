from bs4 import BeautifulSoup
import requests


#----retrieving text from website------
url = "https://coinmarketcap.com/"
result = requests.get(url).text #sent request to get text
doc = BeautifulSoup(result, "html.parser") #run request through beautiful soup

tbody = doc.tbody

trs = tbody.contents #get list of all tags inside table body (rows)

#print(trs[0].next_sibling) #get next table row after first table row

#print(trs[1].previous_sibling) #get previous table row before 2nd table row

#print(list(trs[0].next_siblings)) #look at all table rows after 1st row

#print(trs[0].parent.name) #give name of tag

#print(list(trs[0].descendants)) #gives everything coming after or in tag (contents,children work too)
