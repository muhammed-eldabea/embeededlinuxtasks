class Human () :
    __name   = ""
    __age    = 0
    __weight = 0
    __legnth = 0

    def __init__(self , name ) :
        """
        Used to init the Class with names as a human 
        Passed the Human name and return a class with object
        """
        self.__name  = "" 
        self.__age    = 0 
        self.__weight = 0 
        self.__legnth = 0 
        self.__name = name  
    def SetAge (self,age) :
        """
        Used to set the object Age 
        Para[in] : the age 
        """
        self.__age = age 
    def SetLegnth (self,legnth) :
        """
        Used to set the object legnth 
        Para[in] : the legnth 
        """
        self.__legnth = legnth 
    def SetWeight (self,W) :
        """
        Used to set the object Weight 
        Para[in] : the Weight 
        """
        self.__weight =W
    def printHuman(self) : 
        print(f"{self.__name} age is {self.__age}")
        print(f"{self.__name} Legnth is {self.__legnth}")
        print(f"{self.__name} Wight is {self.__weight}")
    def __del__ (self) :
        print(f"the {self.__name} is being removed now ") 


Mohamed = Human("Mohaed") 

Mohamed.SetAge(15) 
Mohamed.SetLegnth(185)
Mohamed.SetWeight(95) 
print("==================Class Mohamed==================")
Mohamed.printHuman() 
Mohamed.__name = "Mostafa"  #this line have ni impact to the code as python understand it a private member so it Just change the name of thememeber in this line as the following 
"""
You attempt to change Mohamed.__name.
Python internally uses the mangled name (e.g., _Human__name).
Since you're in the same file, Python allows the modification, but it modifies the mangled version, not the original __name attribute.
How to Properly Change Private Attributes:

Here are the recommended ways to modify private attributes while maintaining encapsulation:

Public Setter Methods:
Define a method named set_name that takes the new name as an argument and assigns it to the private __name attribute (potentially with validation).

Python
class Human:
  def __init__(self, name):
    self.__name = name

  def set_name(self, new_name):
    # Add validation logic here (e.g., check for minimum length)
    self.__name = new_namel

# Usage
Mohamed = Human("Mohaed")

Mohamed.set_name("Mostafa")  # This is the recommended way



"""
print("==================Class Mohamed==================")
Mohamed.printHuman() 

print("==================Class Mohamed with changing name to Mostafa==================")
print(Mohamed.__name)
print("==================Class Mohamed after Name chaging==================")

Mohamed.printHuman() 
print("================== dell Class Mohamed==================")

del Mohamed 

print("==================Class Ahmed ==================")

Ahmed = Human("Ahmed") 

Ahmed.SetAge(11) 
Ahmed.SetLegnth(199)
Ahmed.SetWeight(80) 
Ahmed.printHuman() 
print("================== del Class Ahmed ==================")

#all clases are removed if they are not used any more in the Code / or by the end of the code 