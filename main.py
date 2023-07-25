numlist = []

howmany = int(input("How many numbers: "))

for x in range(howmany):
    answer = input("Enter your number: ")
    numlist.append(answer)
    
    
    
def addition():
    x = sum(numlist)
    print(x)
 
def subtraction():
    y = float(numlist[0])
    for x in range(howmany - 1):
        y -= float(numlist[x+1])
    print(y)

def multiply():
    result = 1
    for x in numlist:
        result = result * int(x)
    print(result)

def devide():
    y = float(numlist[0])
    for x in range(howmany - 1):
        y /= float(numlist[x+1])
    print(y)
    
def average():
    x = float(sum(numlist))/howmany
    print(x)
    
addition()
    