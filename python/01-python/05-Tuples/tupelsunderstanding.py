fruits = ("Apple", "Mango" , "Banna" , "Cantalope") 
(green,red,*orange)=fruits 
print(green)  
print(red) 
print(orange)



print("=============== break tuples=========================")
(greenb,*redb,orangeb)=fruits 
print(greenb)  
print(redb) 
print(orangeb)  

print("=================Count/index=======================")

print(fruits.count("Apple"))  
print(fruits.index("Apple"))

print("==============double==========================")

fuitsdouble = fruits *2 

print(fuitsdouble)

