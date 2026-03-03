#file writing
#name
#age 
#gender
#city
#country
f= open("data.txt",'w')
for i in range(2):
    name=input('Enter name :')
    age=input('Enter Age :')
    city=input('Enter city :')
    country=input('Enter country :')
    f.write=(f'\nyour data is {name,age,city,country}')
    f.close()
#file reading
    f= open("data.txt",'a')
    f.write(f'\nyour data is {name,age,city,country}')
    f.close()
#file reading
    f= open("data.txt",'r')
    msg=f.read()
    print(msg)
f.close()

