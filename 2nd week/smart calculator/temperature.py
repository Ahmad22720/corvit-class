def temprature():
  print ('Select 1_c_to_f and select 2_f_to_c')
  choice = input("Enter your choice (1-2): ")
  if choice == '1':
   celsius = float(input("Enter Celsius: "))
   farnhite_ =(celsius * 9/5) + 32
   print("Temperature in Fahrenheit:",farnhite_)

  elif choice == '2':
   farnhite = float(input("Enter farnhite temprature: "))
   celsius_ = (farnhite - 32) * 5/9
   print("Temperature in Fahrenheit:", celsius_)
   
  else:
   print("invalid choice:")
