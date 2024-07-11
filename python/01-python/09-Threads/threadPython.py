import threading as th 
import time as t

TaskCounter = 0 
Task2Flag = False
def Task1() :
    while True : 
        global TaskCounter 
        global Task2Flag
        TaskCounter = TaskCounter + 1   
        if Task2Flag == True :
            Task2Flag = False
            print ("Im Task 1 ") 
        t.sleep(10) 


def Task2() :
    while True :
        global TaskCounter 
        global Task2Flag

        TaskCounter = TaskCounter + 1
        Task2Flag = True   
        print ("Im Task 2 ") 
        t.sleep(2) 

def Task3() :
    while True : 
        global TaskCounter 
        TaskCounter = TaskCounter + 1 
        print ("Im Task 3 ") 
        t.sleep(3) 
# even the tasks are distrubuted in multiple Cores but the python limit the excution of the tasks as 
#python is interprter langunage the once the task is excuted it is only one that runnign in a single time 
#Python Use Global Interpprter Lock GIL >> that allow the thread as one thread will be excuted 
#  

thread1=th.Thread(target=Task1) 
thread2=th.Thread(target=Task2) 
thread3=th.Thread(target=Task3) 

thread1.start() 
thread2.start() 
thread3.start()
while True : 
    print("all thethread are started")
    print(TaskCounter) 
    t.sleep(1)  



 