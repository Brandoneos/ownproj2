
# Importing modules
import math

# Modules ---------------

# Functions ---------------------------
def greet(name):
    print("Hello, " + name + "!")
def ending():
    print("Thanks for using this To-Do List Program\n")
def showList(mylist):
    print("This is your current To-Do List:\n")
    print("---------------------------------\n")
    #show list here
    #dictionary object + while loop
    x = 0
    checkmark = '✓'
    while x < len(mylist):
        x+=1
        if mylist[x-1][1] == 1:
            print(f"{x}(" + checkmark + ") " + mylist[x-1][0])
        else:
            print(f"{x}() " + mylist[x-1][0])
    print("\n")
    print("---------------------------------\n")
def add(mylist):
    print("What would you like to add to the list?\n")
    input1 = input("Input: ")
    pair = (input1,0) # 0 for not marked, 1 for marked
    mylist.append(pair)
def remove(mylist):
    print("What would you like to remove from the list?\n")
    input1 = input("Input: ")
    mylist.pop(int(input1) - 1)
def mark(mylist):
    print("What would you like to mark on the list?\n")
    input1 = input("Input: ")
    if mylist[int(input1) - 1][1] == 1:

        mylist[int(input1) - 1] = (mylist[int(input1) - 1][0],0)
    else:
        mylist[int(input1) - 1] = (mylist[int(input1) - 1][0],1)
        
    
def action(input2,ind,mylist):
    input3 = int(input2)
    if input3 == 1:
        ind = 0
        # print("Added\n")
        add(mylist)
        # Add to the list
    elif input3 == 2:
        ind = 0
        # print("Removed\n")
        remove(mylist)
        # Remove something from list
    elif input3 == 3:
        print("Marked\n")
        mark(mylist)
        ind = 0
        # Mark List
    elif input3 == 4:
        # nothing
        ind = 0
    else:
        # invalid input
        input3 = 0
        ind = 1
        print("Invalid input. Please try again\n")
    return input3, ind
    

def menu(ind):
    if ind == 0:
        print("What would you like to do:\n")
        print("1) Add\n2) Remove\n3) Mark\n4) Exit\n")

# Functions -------------------------