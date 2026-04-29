# initiate class
class vehicle:
    # class attributes
    category ="Transport"
    total_vehicle = 0
    
    # constructor >> instance/object
    def __init__(self,brand,model,year,color,speed):
        print('costructor created')
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
        self.speed=speed
        
        vehicle.total_vehicle += 1

    #object method 1   
    def display_info(self):
        print(f"vehicle name is :{self.brand}")
        print(f"vehicle model is :{self.model}")
        print(f"built year is :{self.year}")
        print(f"color of vehicle is :{self.color}")
        print(f"speed  is :{self.speed}")
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