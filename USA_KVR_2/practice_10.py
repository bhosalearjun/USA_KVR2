def sumop(a,b):
    c=a+b
    return c

x=float(input("enter the first value:"))
y=float(input("enter the second  value:"))

result=sumop(x,y)

print("sum of {} and {} is {}".format(x,y,result))