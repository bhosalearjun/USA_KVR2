def disp(sno,sname,*kvr,city="PUNE"):
    print("-" * 50)
    print("student number={}".format(sno))
    print("student name={}".format(sname))
    print("student city=",city)
    sum=0
    for val in kvr:
        print("\t{}".format(val))
        sum=sum+val
    print("sum=",sum)



disp(100,"JK",10,20,30,40,50)
disp(200,'RJ',10,20,30,40)
disp(300,'SS',10,20,30)
disp(400,'DK',10,20)
disp(500,'QK',10)
disp(600,'MM')