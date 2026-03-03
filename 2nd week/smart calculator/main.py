# --- SMART CALCULATOR ---
import arithmetic
import bmi
import length
import temperature
while True :
    # 1. Show the Menu
    print("\n--- MENU ---")
    print("1. ARithmetic oprations")
    print("2. BMI Calculator")
    print("3. Temprature")
    print("4. Find length")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    # 2. Handle the Choice
    if choice == '1':
       arithmetic.arithmetic()
    elif choice == '2':
       bmi.bmi_calculator()    
    elif choice == '3':
        temperature.temprature()
    elif choice == '4':
        length.length()
    elif choice == '5':
        print("Exiting... Goodbye!")
    else:
        print("Invalid choice, try again.")
