def setOrNot(number,n):
    if number &(1<<(n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")
number=int(input("enter a number: "))
n=int(input("enter a position: "))
setOrNot(number,n)