class Human :
    __classname = "Human"

    def Class_print (self):
        print(self.__classname)





h1=Human() 

h1.__classname = 500

print(h1.__classname)

h1.Class_print()