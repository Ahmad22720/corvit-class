#initiate class
class Student:
    department_name= "Information Technology"
    total_students = 0
    
    #attributes
    def __init__ (self,name,age,roll_no,program,gpa,semester):
       self.name = name
       self.age = age
       self.roll_no = roll_no
       self.program = program
       self.gpa = gpa
       self.semester = semester
    
       Student.total_students +=1
    
    # insistance method 1
    def display_profile(self):
        print(f"student name is : {self.name}")
        print(f"student Age is : {self.age}")
        print(f"student's Roll no is : {self.roll_no}")
        print(f"program is : {self.program}")
        print(f"student's gpa is : {self.gpa}")
        print(f"student's semester is : {self.semester}")
     # insistance method 2
    def update_semester(cls,semester):
        cls.semester=semester
        print('updated semester is :',semester)
        # insistance method 3 
    def submit_assignment(self):
       print("Assignment submitted")
       # insistance method 4 
    def take_quiz(self,number):
       if (2+2==number):
         print('student is pass in quiz')
       else:
           print('You are fail')

#class method
         
s1=Student("Ali",25,1,'BSIT',2.9,'4th semester')
s1.display_profile()
s1.submit_assignment()
number=int(input('Enter number to Answer what is 2+2=? :'))
s1.take_quiz(number)
s1.update_semester('5th semester')
s2=Student("Ahmad",26,2,'BS physics',3,'4th Semester')
s2.display_profile()