def disp_student_info(sno,sname,sclass,**subjectmarks):
    print("-"*50)
    print("sno=",sno)
    print("name=",sname)
    print("class=",sclass)
    print("marks are as follows")
    sum=0
    for sub,marks in subjectmarks.items():
        print(f"{sub}--{marks}")
        sum=sum+marks
    print("sum=",sum)








disp_student_info(10,"JK",'12TH',HINDI=88,MARATHI=90,MATHS=80,ENGLISH=95)
disp_student_info(sno=20,sname='SS',sclass='12TH',MARATHI=88,SANSKRIT=98,HISTORY=49,GEOGRAPHY=69)
disp_student_info(sclass='BE',sno=30,sname='MT',M1=88,TE=78,ML=96,FE=89,CAD=78)