# bancore.py
branch_id = 2057
user_number = 1

users_info = {}  # dictionary to store users_info

def create_account(name, password):
   global user_number
   customer_id = f"{branch_id}-{user_number}"
   users_info[customer_id]={"name":name,"password":password}
   print("Account created successfully :")
   print("Your Customer id is :",customer_id)
   user_number +=1
   return customer_id
def login(customer_id,name ,password):
   if customer_id in users_info:
       if users_info[customer_id]["name"] == name and users_info[customer_id]["password"] == password:
           print('login succussful ')
           return True
   print ('Invalid login')
   return False