
# Import Helper file
import helper

# Prompt: Make a todo list program, where the user can add, remove, and mark things to do in a list

# Main Function

def main():
    mylist = []
    input1 = 0
    ind = 0
    while input1 != 4:
        helper.menu(ind)
        
        input1 = input("Input: ")
        # print("input1: " + input1 + "\n")
        input1, ind = helper.action(input1,ind,mylist)
        helper.showList(mylist)
    helper.ending()
# Calling Main

main()

