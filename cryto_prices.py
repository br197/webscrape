from bs4 import BeautifulSoup
import requests


#----retrieving text from website------
url = "https://coinmarketcap.com/"
result = requests.get(url).text #sent request to get text
doc = BeautifulSoup(result, "html.parser") #run request through beautiful soup

tbody = doc.tbody #gives table body
trs = tbody.contents #get list of all tags inside table body (rows)

prices = {}

for tr in trs[:10]: #loops through table rows for prices
   # for td in tr.contents[2:4]: #loop through table data in table rows (all td tags) for name and price
    name,price = tr.contents[2:4] #store data in name,price variables
    #print(name.p.string) #get names in p tags
    fixed_name = name.p.string
   # print(price.a) #look at price in a tag
    #print(price.a.string) #get prices of names in a tag
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price #dictionary link fixed_name key to price value

print(prices)