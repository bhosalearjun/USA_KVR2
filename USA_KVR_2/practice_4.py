n=int(input("enter how many tables you want to print:"))

if(n<=0):
    print("please enter valid input")
else:
    for num in range(1,n+1):
        print("-"*50)
        print("multplication table for {}".format(num))
        print("-"*50)

        for i in range(1,11):
            print("{}*{}={}".format(num,i,num*i))

