##Jonathan Brown
##List Traversal and Exception Handling
##CSCD-110
##Homework 5

#______________________________________________________________________________
def main():
    theList = []
    choice = displayMenu()
    
    while choice != '6':
        if choice == '1':
            addNum(theList)
        elif choice == '2':
            mean(theList)
        elif choice == '3':
            median(theList)
        elif choice == '4':
            print(theList)
        elif choice == '5':
            print(theList[::-1])
        choice = displayMenu()
        
    print("\nThanks for playing!\n\n")

#_____________________________________________________________________________       
def displayMenu():
    myChoice = '0'
    while myChoice != '1' and myChoice != '2' \
        and myChoice != '3' and myChoice != '4' \
        and myChoice != '5' and myChoice != '6':
        print("""\n\nPlease choose:
                1. Add a non-negative integer to the list
                2. Display the mean                       
                3. Display the median
                4. Print the list
                5. Print the list in reverse order
                6. Quit""")
        myChoice = input("Enter option--> ")
        
        if myChoice != '1' and myChoice != '2' and \
            myChoice != '3' and myChoice != '4' and \
            myChoice != '5' and myChoice != '6':
            print("Invalid option. Please select again.")
            
    return myChoice

#_____Add a num to the list/array_____________________________________________
def addNum(theList):
    while True:
        try:
            addNum = int(input("Enter a non-negative integer: "))
            if addNum < 0:
                raise ValueError
            break
        except:
            print("I'm sorry that is not a non-negative integer.")
    theList.append(addNum)
    
#______Display the Mean________________________________________________________
def mean(theList):
    mean = 0
    length = len(theList)
    total = 0
    if length > 0:
        for item in theList:
            total = total + item
        mean = total / length
    print("The mean is:", mean)
              
#______Display the Median______________________________________________________
def median(theList):
    theList.sort()
    length = len(theList)
    if length == 0:
        median = 0
    elif length % 2 == 0 and length > 0:
        median = (theList[length // 2] + theList[length // 2 - 1]) / 2
    else:
        median = theList[length // 2]
    print("the median is:", median)
        
#______________________________________________________________________________
main()
