# Calling each function
import bmi
import calculator
import temprature_converter
import password_checker_using_if_else
print("Choose calculator: 1-BMI, 2-Simple, 3-Temp, 4-pssword chekcer ")
choice = int(input("Enter choice: "))

if choice == 1:
    bmi.bmi_calculator()
elif choice == 2:
    calculator.simple_calculator()
elif choice == 3:
    temprature_converter.temp_converter()
elif choice == 4:
    password_checker_using_if_else.password_check()
else:
    print("Invalid choice")