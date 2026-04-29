# initiate class
class Student:
    # class attributes
    school_name="Corvit"
    total_students=0
    
    # constructor >> instance/object
    def __init__(self,name,roll_no,age,course,marks):
        print('costructor created')
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.course=course
        self.marks=marks
        
        Student.total_students += 1

    #object method 1   
    def display_info(self):
        print(f"student name is :{self.name}")
        print(f"student roll no  is :{self.roll_no}")
        print(f"student age  is :{self.age}")
        print(f"student marks are :{self.marks}")
        print(f"student course is :{self.course}")
    # object method 2
    def study(self):
        print(self.name, "is studying")
        
        #object method 3
    def take_exam(self):
        print(self.name,"is taking an exam :")
        
   # class method 1
    def get_total_students(cls):
       print('total students :',cls.total_students)
       
    #class method 2
    def change_school_name(cls,name):
       cls.school_name=name

# create an object for the student
s1=Student("Ahmad",12,25,45,'iT')
s1.display_info()
s1.study()
s1.take_exam()
s2=Student("Ahmar",2,24,65,'English')
s3=Student("Ali",1,27,79,'CS')
s4=Student("Ahad",16,25,89,'Phsyics')
s1.get_total_students()