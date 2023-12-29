import csv

with open("studentmarks.csv","w",newline='') as s:
    w=csv.writer(s)
    w.writerow(["student_rollno","student_name","telugu marks","English marks","Maths_marks","Hindi_marks","Science_marks","Social_marks","Total_marks","Average_marks","Percentage","Result"]) 

    n=int(input("enter number of students  entry details: "))
    for i in range(1,n+1):
        print(i," STUDENTS MARKS DEATILS ")
        sturollno=int(input("enter rollno :"))
        stuname=input("enter name : ")
        telugu=int(input("enter telugu marks :"))
        english=int(input("enter english marks : "))
        maths=int(input("enter maths marks :"))
        hindi=int(input("enter hindi marks :"))
        science=int(input("enter science marks :"))
        social=int(input("enter social marks:"))
        a=(telugu+english+maths+hindi+science+social)
        total=a
        b=a/5
        avg=b
        c=a/600*100
        per=c
        result="pass"if per>=35 else "fail"
        w.writerow([sturollno,stuname,telugu,english,maths,hindi,science,social,total,avg,per,result])


    print("totsl students data written to csv file ")