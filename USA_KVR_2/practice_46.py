def disp(**kwargs):
    print("-"*50)
    for key,val in kwargs.items():
        print("{}------->{}".format(key,val))




disp(sn=10,sname='JK',city='pune')
disp(tname='KVR',city='HYD')
disp(inst='NARESH',mobile=551515484)