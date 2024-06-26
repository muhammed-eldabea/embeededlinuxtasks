
#inial creation for the funcction 
def myfunction() :
    print ("my name is mohammed eldabaa") 
myfunction()  


#how to pass argument 
def myfunction(name) :
    print (f"my name is {name}")
myfunction("Mohamed eldabaa")  

#how to pass argument and not pass any argument as set the defualt  
def myfunction(name="Maio") :
    print (f"my name is {name}")
myfunction("Mohamed eldabaa")  
myfunction()  


#how to pass multi argument 
def myfunction(*name) :
    print ("Type of the input " , end=" ") 
    print(type(name))
    print (f"my name is {name[0]}")
    print (f"my name is {name[1]}")
    print (f"my name is {name[2]}") 
myfunction("Mohamed " , "eldabaa" , "hashem")  


#de-seralize the data 
def myfunction(**name) :
    print ("Type of the input " , end=" ") 
    print(type(name))
    print (name["First_Name"]  )
    print (name["Family_name"] )
    print (name["Last_Name"]   ) 
myfunction(First_Name="Mohamed " , Family_name="eldabaa" ,Last_Name= "hashem")  

