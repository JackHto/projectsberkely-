def cOq():
    question = input("(C)ontinue or (Q)uit: ")
    if question.upper() == "C":
        calculator()
    elif question.upper() == "Q":
        exit()
    else:
        print("invalid")
        cOq()
            
def calculator():
    numlist = []

    howmany = input("How many numbers: ")
    try:
        howmany = int(howmany)
    except:
        print("invalid")
        calculator()
    

    for x in range(howmany):
        answer = input("Enter your number: ")
        try:
            answer = float(answer)
            numlist.append(answer)
        except:
            print("invalid")
            calculator()
        
        
    def addition():
        x = sum(numlist)
        print(x)
        cOq()
    
    def subtraction():
        y = float(numlist[0])
        for x in range(howmany - 1):
            y -= float(numlist[x+1])
        print(y)
        cOq()

    def multiply():
        result = 1
        for x in numlist:
            result = result * int(x)
        print(result)
        cOq()

    def devide():
        y = float(numlist[0])
        for x in range(howmany - 1):
            y /= float(numlist[x+1])
        print(y)
        cOq()
        
    def average():
        x = float(sum(numlist))/howmany
        print(x)
        cOq()
        

    wfun = input("What function, (A)ddition, (S)ubtraction, (M)ultiply, (D)evide, (AV)erage): ")


    if wfun.upper() == "A":
        addition()
    elif wfun.upper() == "S":
        subtraction()
    elif wfun.upper() == "M":
        multiply()
    elif wfun.upper() == "D":
        devide()
    elif wfun.upper() == "AV":
        average()
    else:
        print("not a valid operation")
        cOq()
        
calculator()