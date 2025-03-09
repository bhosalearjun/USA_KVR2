def disp(*kvr):
    print("-"*50)
    print("number of values={}".format(len(kvr)))
    for val in kvr:
        print("\t{}".format(val))




disp(10,20,30,40,50)
disp(10,20,30,40)
disp(10,20,30)
disp(10,20)
disp(10)
disp()