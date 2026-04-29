from car import Car
from customer import Customer
from rental_service import RentalService
from bike import Bike
from add_customer import add_customer
#--------------------------
 # Main Program
#------------------------
service= RentalService()
#add vehicle
bike1=Bike('B101','Honda',2020,1000,'70cc','petrol')
bike2=Bike('B102','sutlej',2015,1000,'125cc','petrol')
car1=Car('C101','Honda',2016,3000,'660cc','petrol')
car2=Car('C103','Suzuki',2026,4000,'1200cc','petrol')

#service.add_vehicle(bike1)
service.add_vehicle(bike2)
service.add_vehicle(car1)
#service.add_vehicle(car2)

#Register Customers
customer1=Customer('u1','Ahmad')
customer2=Customer('u2','Ali')

service.register_customer(customer1)
service.register_customer(customer2)
while True:
    print('\n Vehicle Rental System :')
    print('1. Show available vehicles :')
    print('2. Rent a vehicle :')
    print('3. Return a vehicle:')
    print('4. View customer details:')
    print('5. Show all vehicles :')
    print('6. Search vehicle by id :')
    print('7. Add customer :')
    print('8. Exit :')
    choice = input('Enter your choice :')
    
    if choice == '1':
        service.show_available_vehicles()
    elif choice == '2':
        c_id=input('Enter customer id :')
        v_id= input('Enter Vehicle id :')
        days= int(input('For how much time in days you want to hire vehicle:'))
        service.rent_vehicle(c_id,v_id,days)
    
    elif choice == '3':
        c_id = input ('Enter Customer id :')
        service.return_vehicle(c_id)
    
    elif choice == '4':
        service.view_customer_details()
    
    elif choice == '5':
        service.show_all_vehicles()
    elif choice == '6':
        v_id = input('Enter Vehicle id :')
        service.search_vehicle_by_id(v_id)
    elif choice == '7':
        add_customer(service)
    elif choice == '8':
        print('Thank You for using Rental system')
        break
    else:
        print('invalid choice :')