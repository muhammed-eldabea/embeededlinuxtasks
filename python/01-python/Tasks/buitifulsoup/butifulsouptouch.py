import bs4 as bs
import time   as ts
import requests as req 


htmlconttent = req.get("http://http://localhost:5500/python/01-python/Tasks/buitifulsoup/").content 
print(htmlconttent) 