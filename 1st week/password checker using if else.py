default_password=1246
user_name=input('Enter username:')
password=int(input('Enter password :'))
while(password != default_password):
        print('Enter correct password :')
        password=int(input('Enter password :'))
print('Successful logged in:')