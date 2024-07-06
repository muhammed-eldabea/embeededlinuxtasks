class Human () :
    __name  = "" 
    __age    = 0 
    __weight = 0 
    __legnth = 0 ; 

    def __init__(self , name ) :
        """
        Used to init the Class with names as a human 
        Passed the Human name and return a class with object
        """
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

class man(Human):
    __Hopppy=[]
    def __init__(self, name,age=18,len=180,w=87):
        super().__init__(name)
        self.SetAge(age)
        self.SetLegnth(len)
        self.SetWeight(w)   
    def AddHoppy(self,hoppy) :
        self.__Hopppy.append(hoppy) 
    def printHoppy(self):
        for i in self.__Hopppy :
            print(i)


Mohamed = man("Mohamed") 
Mohamed.AddHoppy("Tennis Table")
Mohamed.AddHoppy("Fotball")
# Mohamed.printHoppy() 
Mohamed.printHuman() 


















# Mohamed = Human("Mohaed") 

# Mohamed.SetAge(15) 
# Mohamed.SetLegnth(185)
# Mohamed.SetWeight(95) 
# Mohamed.printHuman() 

# del Mohamed 

# Ahmed = Human("Ahmed") 

# Ahmed.SetAge(11) 
# Ahmed.SetLegnth(199)
# Ahmed.SetWeight(80) 
# Ahmed.printHuman() 





#all clases are removed if they are not used any more in the Code / or by the end of the code 