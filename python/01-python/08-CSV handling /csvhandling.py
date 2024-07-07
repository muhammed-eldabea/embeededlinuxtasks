import csv 

try :
    with open("/home/maio/embeededlinuxtasks/python/01-python/08-CSV handling /Data.csv","r") as f :
        data =csv.reader(f)  
        for row in data :
            print(row) 
except FileExistsError:
    print ("the file is not found")