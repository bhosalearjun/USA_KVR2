def sumop():
    a=float(input("enter the first value:"))
    b=float(input("enter the second value:"))
    c=a+b
    return a,b,c

x,y,z=sumop()

print("sum of {} and {} is {}".format(x,y,z))


print("-"*50)

res=sumop()
print(res,type(res))

print("sum of {} and {} is {}".format(res[0],res[1],res[2]))