def disp(x):
    if(type(x)!=dict):
        print(x)
        print("type of object=",type(x))
        for val in x:
            print(val)
    else:
        for k,v in x.items():
            print("{}---------->{}".format(k,v))


lst=[1,2,3,"PYTHON",True,"C"]

disp(lst)

print("-"*50)

tpl=('will','win',3)
disp(tpl)

print("-"*50)

s1={'this','will','work','trust','the','god'}
disp(s1)

print("-"*50)

fs1=frozenset({'this','will','work','trust','the','god'})
disp(fs1)

print("-"*50)
d1={1:"Python",2:"JAVA",3:"C"}
disp(d1)