# class
class Employee:


      name="nagasiva" 


      def __init__(self,ename,esal,eid,epack,edomain,name):


            name="nagasiva"


            self.ename=ename


            self.esal=esal


            self.eid=eid


            self.epack=epack


            self.edomain=edomain


            self.name=name


      def employeeDetails(self) :


            print("Employee Details:")   


            print(self.name,"---------",self.ename,"--------",self.esal,"--------",self.eid,"-------",self.epack,"-------",self.edomain) 





e=Employee("nagasiva",1000,101,35,".net","jagan")


e.employeeDetails()


print(e.name)


print(Employee.name)





e=Employee("shanwith",2000,201,45,"sap","durga")


e.employeeDetails()


print(e.name)


print(Employee.name)








class student:


  def __init__(a,x,y,z,r) :


    a.snm=x


    a.srno=y


    a.sper=z 


    a.sclg=r





  def display(a):


      print("display method....")


      print(a.snm)


      print(a.srno)


      print(a.sper)


      print(a.sclg)


s=student("nagasiva",456,24,"ramesh")


s.display()








class Employee:


    def __init__(emp) :


        emp.ename="nagasiva"


        emp.esal=1000


        emp.eid=101


        emp.epack=5.0


    def employeeDetails(emp):   


        print("Employee Details:") 


        print(emp.ename)


        print(emp.esal)


        print(emp.eid) 


        print(emp.epack)


Employee().employeeDetails() 





# #by using method


class Student:


    def studentRecords(self,sname,srno,sper):


        self.sname=sname


        self.srno=srno


        self.sper=sper


        print("student records")


s=Student()


s.studentRecords("nagasiva",45,65)     











# #by  using constructor





class Student:


    def __init__(self,sname,srno,sper):


        self.sname=sname


        self.srno=srno


        self.sper=sper


        print("student records")


s=Student("nagasiva",45,65)





# #by using constructor and method


class Student:


    def __init__(self,sname,srno,sper):


        self.sname=sname


        self.srno=srno


        self.sper=sper





    def studentRecords(self,sname,srno,sper):


        self.sname=sname


        self.srno=srno


        self.sper=sper


        print("student records")


Student("durga",56,98)  .studentRecords("durga",56,98) 
