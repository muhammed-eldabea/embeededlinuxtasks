filedata = open("/home/maio/embeededlinuxtasks/python/01-python/07-Files Hanldinmg /file.txt" , "r") 


print("===================Reading the files contecnt with Readline then reset the seek  ==========================")

line1 = filedata.readline()  
print(line1) 

line2 = filedata.readline()  
print(line2) 


print(filedata.tell() ) 
filedata.seek(0)  #used to reset the Pointer to the file 


print("===================Reading the files contecnt with Readlines ==========================")

datafromthefile = filedata.readlines() 

for i in datafromthefile :
    print(i)   

filedata.close() 



print("===================Updating the file content ==========================")

filedata = open("/home/maio/embeededlinuxtasks/python/01-python/07-Files Hanldinmg /file.txt" , "r+") 

print(len(filedata.readlines()))

# # filedata.seek(0,2)   

filedata.write("Wririting from the Python script") 
filedata.close() 

print("===================Reding from the file after wrirting ==========================")

filedata = open("/home/maio/embeededlinuxtasks/python/01-python/07-Files Hanldinmg /file.txt" , "r") 
datafromthefile = filedata.readlines() 
for i in datafromthefile :
    print(i)
    # # print(" ")   

filedata.close() 
