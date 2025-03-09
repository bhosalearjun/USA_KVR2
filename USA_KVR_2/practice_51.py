def disp_student_info(sno,sname,sclass,*vals,city="MUMBAI",**subjectmarks):
    print("-"*50)
    print("sno=",sno)
    print("name=",sname)
    print("class=",sclass)
    print("city=",city)
    print("variable length argumets={}".format(vals))
    if(len(subjectmarks)>0):
        print("marks are as follows")
        sum=0
        for sub,marks in subjectmarks.items():
            print(f"{sub}--{marks}")
            sum=sum+marks
        print("sum=",sum)
    else:
        print("-"*50)




disp_student_info(10,"JK",'12TH',25,35,45,55,HINDI=88,MARATHI=90,MATHS=80,ENGLISH=95)
disp_student_info(20,'SS','12TH',2,4,6,MARATHI=88,SANSKRIT=98,HISTORY=49,GEOGRAPHY=69)
disp_student_info(30,'MT','BE',66,80,M1=88,TE=78,ML=96,FE=89,CAD=78)
disp_student_info(500,'Qanutum','Research',5,6 ,city='USA')
disp_student_info(600,"KVR","TRAINER")