def fun(x) :
    print("the Value of X from the function is " , x) 
    print(f"the adrees of X from function is {id(x)}") 

def funglobalx() :
    global x 
    print("the Value of X from the funglobalx is " , x) 
    print(f"the adrees of X from funglobalx is {id(x)}") 

def funlocalx() :
    x = 20  
    print("the Value of X from the funlocalx is " , x) 
    print(f"the adrees of X from funlocalx is {id(x)}") 



x = 10 

print (x)
print (id(x)) 

fun(x) 
print (x)
print (id(x)) 
funlocalx() 
funglobalx()

print("===========================Lists========================================")

def funlist(x) :
    print("the Value of X from the function is " , xlist) 
    print(f"the adrees of X from function is {id(xlist)}") 

def fungloballist() :
    global xlist  
    print("the Value of X from the funglobalx is " , xlist) 
    print(f"the adrees of X from funglobalx is {id(xlist)}") 

def funlocallist() :
    xlist[0] = 20  
    print("the Value of X from the funlocalx is " , xlist) 
    print(f"the adrees of X from funlocalx is {id(xlist)}") 

def funlocallistb(xlist) :
    xlist[0] = 20  
    print("the Value of X from the funlocalx is " , xlist) 
    print(f"the adrees of X from funlocalx is {id(xlist)}") 


xlist = [10] 

print (xlist)
print (id(xlist)) 

funlist(xlist) 
print (xlist)
print (id(xlist)) 
funlocallist() 
fungloballist()
funlocallistb(xlist)

#note that the address of the x even in the function is the same address of the global one 