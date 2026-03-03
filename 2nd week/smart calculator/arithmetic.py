def arithmetic():
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
        
