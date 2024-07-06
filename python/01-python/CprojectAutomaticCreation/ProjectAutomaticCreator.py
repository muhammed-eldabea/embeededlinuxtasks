import os 
import shutil 


#clean the dirctory
if os.path.exists("Project") :
    shutil.rmtree("Project") 
    print( "the project Folder is Found and Removed ") 

#creat the folder structure 
os.system("mkdir -p Project/src")
os.system("mkdir -p Project/tests")
os.system("mkdir -p Project/build")

#creat the main file 
os.system("touch  Project/src/main.cpp")
#creat the cmake build file list 
os.system("touch  Project/CMakeLists.txt") 

file = open("Project/src/main.cpp","a") 
file.write("""#include <iostream> \n  
           
           int main() { \n
             std::cout <<"Hello From the Automatic Script" ; \n  
               return 0 ; \n

           \n } 
           \n 
           
        
           """) 

file.close() 

fd=open("Project/CMakeLists.txt","w")
os.write(fd.fileno(),"""cmake_minimum_required(VERSION 3.10)\n
         
         project(helloWorld) \n 
         add_executable (helloWorld src/main.cpp)
         
         """.encode()) 
os.chdir("Project/build") 
os.system("cmake .. && make -j && ./helloWorld") 
print("\n Buiding the Project is done ")
