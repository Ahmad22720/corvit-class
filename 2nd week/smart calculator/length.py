def length():
    # 1. Show the Menu
  print("\n--- MENU ---")
  print("1. meters to kilometer")
  print("2. kilometers to meters")
  print("3. meters to feet")
  print("4. feet to meters")
  print("5. Exit")
    
  choice = input("Enter your choice (1-5): ")
  if choice == '1':
   meter = float(input("Enter meters: "))
   kilometer= meter/1000
   print("The length in kilometers is:",kilometer)

  elif choice == '2':
   km = float(input("Enter kilometers: "))
   meters= km*1000 
   print("The length in meters is:",meters)

  elif choice == '3':
   m= float(input("Enter meters: "))
   feet= m*3.280 
   print("The length in feet is:",feet)

  elif choice == '4':
   f= float(input("Enter feets: "))
   m= f/3.280 
   print("The length in meters is:", m)

  else:
   print("invalid choice:")
