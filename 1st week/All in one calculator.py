#Bmi calcultaor using for loop
def bmi_calculator():
  weight=float(input('enter a value of weight in kgs:'))
  height=float(input('enter a value of height in inches:'))
  h_=height*0.3048
  bmi = weight / (h_ ** 2)
  print('your BMI is:',bmi)
  if(bmi<18.5):
    print('you are undrweight:')
  elif(18.5<bmi<25):
    print('you are undrweight:')
  elif(25<bmi<30):
    print('you are overweight:')
  else:
    print('you are obese:')
#math caluclator using  loop

def simple_calculator():
  num1=int(input('Enter 1st number : '))
  num2=int(input('Enter 2nd number : '))
  operator=input('Enter operator from :-,+,/,%,*,<,>,=:  ')
  if(operator=='+'):
     result=num1+num2
     print('The result is: ',result)
  elif (operator == '-'):
     result =num1-num2
     print('The result is: ',result)
  elif (operator=='/'):
    if(num2==0):
     print('divided by zero')
    else:
     result=num1/num2
     print('The result is: ',result)
  elif (operator=='*'):
     result=num1*num2
     print('The result is: ',result)

  elif (operator=='%'):
         if(num2==0):
             print('divided by zero')
         else:
             result=num1%num2
             print('The result is: ',result)
  elif (operator=='='):
     if(num1==num2):
      print('The result is that numbers are equal: ')
     else:
      print('the numbers  are not equal')
  elif (operator=='<'):
     result=num1<num2
     print('The result is: ',result)
  elif (operator=='>'):
     result=num1>num2
     print('The result is: ',result)
  else:
     print('invalid operator')
        
#min max  using for loop
def min_max():
  min=int(input('enter the minimum number :'))
  max=int(input('enter the maximum number :'))
  num=min
  count=int(input('enter the number to count :'))
  for num in range(min, max,2):
    print('series is :',num)
   # num=num+2
  for num in range(count):
    print('Ahmad:',num)
    num=num+2
#Tbale using for loop    
def table_printer():
  num1=int(input('Enter number : '))
  i=1
  print('Table of',num1)
  for i in range (1,11):
    num=num1*i
    print(num1,'*',i,'=',num)
            
#tempratur calculatorusing if else loop
def temp_converter():
  celsius=float(input('enter a value:'))
  c_= celsius
  kelvin= c_+273.15
  farnhite= 9/5*c_+32
  if (c_< 10):
   print('weather is cold:')
  if (c_>30):
   print('weather is hot:')
  else:
   print('its rain today')
                      
  print('temprature in fanhite is :',farnhite)
  print('temprature in fanhite is :',kelvin)    
#password chechker
def password_check(): 
  default_password=1246
  user_name=input('Enter username:')
  password=int(input('Enter password :'))
  while(password != default_password):
        print('Enter correct password :')
        password=int(input('Enter password :'))
  print('Successful logged in:')
 
# Calling each function
print("Choose calculator: 1-BMI, 2-Simple, 3-Math, 4-Temp, 5-table, 6-pssword chekcer ")
choice = int(input("Enter choice: "))

if choice == 1:
    bmi_calculator()
elif choice == 2:
    simple_calculator()
elif choice == 3:
    table_printer()
elif choice == 4:
    temp_converter()
elif choice == 5:
    table_printer()
elif choice == 6:
    password_check()
else:
    print("Invalid choice")
