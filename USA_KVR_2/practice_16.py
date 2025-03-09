def multable(n):
    if(n<=0):
        print("please enter valid number")
    else:
        print("multiplication table for {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("{} * {} ={}".format(n,i,n*i))
            print("-"*50)




x=int(input("enter the number:"))

multable(x)