def power(a,b):
    if (b==1):
        return(a)
        if b != 1:
            return (a*b(a,b-1))
        base = int(input("Enter exponential value: "))
        print ("Result: ",power(a,b))