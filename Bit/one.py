def numOfBits(n):
    ones=0
    zeros=0

    while(n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print(f"number of ones is: {ones}\n Number of zeros is: {zeros}")

number=int(input("enter a number: "))
numOfBits(number)