i=1
while(i<=5):
    print("-"*50)
    print("outer loop i={}".format(i))
    print("-"*50)
    j=1
    while(j<=3):
        print("inner loop j={}".format(j))
        j=j+1
    else:
        i=i+1
        print("out of inner loop")
print("out of outer loop")


