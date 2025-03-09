for i in range(1,6):
    print("-" * 50)
    print("outer loop value of i={}".format(i))
    print("-"*50)
    for j in range(1,4):
        print("inner loop value of j={}".format(j))

    print("out of inner loop")

print("out of outer loop")