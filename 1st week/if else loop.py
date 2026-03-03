marks = float(input('enter a number:'))
if (0<=marks<= 100):
    print("Please enter a number between 0 and 100")
    if (marks >= 90):
        print("your grade is A")
    elif (marks >= 80):
        print("your grade is B")
    elif (marks >= 70):
        print("your grade is C")
    elif (marks >= 60):
        print("your grade is D")
    else:
        print("your grade is F")
else:
  print('enter a valid number')