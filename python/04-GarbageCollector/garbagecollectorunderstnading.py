
list1 = [1,2,4,5,6,7]    
print(id(list1))
list1.append(8) 
print(id(list1))

#after a new asiignation for the same list the data is allocated in 
# diffrent memory location 
#we Can understand the the garabge collector is activatied after every new assignation for the variales 
#in JAVA it is workign after the memory is saturated 
list1 = [11,12,14,15,16,17]
print(id(list1))
list1.append(8) 
print(id(list1))