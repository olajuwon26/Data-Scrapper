import urllib.request
import json
from bs4 import BeautifulSoup

url = "https://old.reddit.com/top/"
headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
#download the URL and extact the content to the variable html
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()
#pass the HTML to Beautifulsoup
soup = BeautifulSoup(html,'html.parser')
#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div",attrs={'id':'siteTable'})
#Now we go into main_table and get every a element <a class="title">
links = main_table.find_all("a",class_="title")
#from each link extract the text of the link and  the link itself
#List to store a dict of data we extracted
extracted_records = []
for link in links:
    title = link.text
    url = link ['href']
    #There are better ways to check if a URL is absolute in Python. For sake
    #of simplicity we'll just stick to .startwith method of a string 
    if not url.startswith('http'):
        url = "https://reddit.com"+url 
    # You can join urls better using urlparse library of python.
    print("%s - %s"%(title,url))
    record = {
     'Title':title,
    'URL':url
    }
    extracted_records.append(record)
with open('data.json', 'w') as outfile:
    json.dump(extracted_records, outfile, indent=4)

print (extracted_records)
    
    
