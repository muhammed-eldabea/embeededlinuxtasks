from bs4 import BeautifulSoup as  bs
import time   as ts
import requests as req 


htmlconttent = req.get("http://localhost:5500/python/01-python/Tasks/buitifulsoup/index.html").content 
#print(htmlconttent) 

soup=bs(htmlconttent,"lxml") 
# print(soup) 


print("=============Paragraph=================")
datacontent = soup.findAll("article" , {"class":"w3-container"} )


# datacontent2 = soup.findAll("p","article" ) 


for paragraph in datacontent:
    print(paragraph.find("h2").text) 

# print("=============Paragraph all =================")

# for paragraph in datacontent2:
#     print(paragraph.text) 


# print(type(datacontent))
# print("=============CityNames=================")
# headrers = soup.find_all("h2") 

# for heardh in headrers:
#     print(heardh.text) 