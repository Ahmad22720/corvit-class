# initiate class
class student:
    # constructor >> instance/object
    def __init__(self,name,roll_no,marks,subject):
        print('costructor created')
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.subject=subject
    
    def tell_intro(self):
        print('intro is :')
        print(f"my name is :{self.name}")
        print(f"my roll no  is :{self.roll_no}")
        print(f"my marks are :{self.marks}")
        print(f"my subject is :{self.subject}")

std1=student('ali',12,35,'english')
print(std1.name)
print(std1.marks)
#emp1=student.tell_intro()
print(std1.subject)
'''
std2=student('ahmad',35,38,'english')
print(std2.name)
print(std2.marks)
#emp1=student.tell_intro()
print(std2.subject)'''

print(std1.tell_intro())        