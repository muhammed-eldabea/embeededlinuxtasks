import requests 

url = requests.get("https://api.ipify.org/?format=json") 
CurrentIP = url.json()["ip"] 
CurrentLocation =  requests.get(f"https://ipinfo.io/{CurrentIP}/geo")

#print(CurrentLocation.json()) 


print( f"Your Current country is : {CurrentLocation.json()['country']}")
print( f"Your Current Region is : {CurrentLocation.json()['region']}")
print( f"Your Current Ciry is : {CurrentLocation.json()['city']}")