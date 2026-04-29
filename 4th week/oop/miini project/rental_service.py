
# Rental service class
class RentalService:
    def __init__(self):
        self.vehicles= []
        self.customers = []
    
    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)
    
    def register_customer(self,customer):
        self.customers.append(customer)
    def show_available_vehicles(self):
        print('\nAvailable Vehicles\n')
        found = False
        for v in self.vehicles:
            if v.is_available:
                found = True
                v.display_info()
        if not found:
            print('No vehicle is available.')

    def show_all_vehicles(self):
        print('\nAll Vehicles\n')
        if not self.vehicles:
            print('No vehicles in system.')
            return
        for v in self.vehicles:
            v.display_info()
            print('Status :', 'Available' if v.is_available else 'Rented')
    
    def rent_vehicle(self,customer_id,vehicle_id,days):
        customer = None
        vehicle = None
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id :
                vehicle = v
        
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
        
        if customer and vehicle and vehicle.is_available:
            vehicle.rent()
            customer.rent_vehicle(vehicle)
            cost= vehicle.calculate_rental_cost(days)
            print('total rental cost :',cost,'Pkr')
        else:
            print('vehicle not available or customer not found :')

    def search_vehicle_by_id(self,vehicle_id):
        vehicle = None
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                vehicle = v
                break
        if not vehicle:
            print('Vehicle not found.')
            return
        vehicle.display_info()
        print('Status :', 'Available' if vehicle.is_available else 'Rented')
            
    def return_vehicle(self,customer_id):
        
        customer =None
        # Find customer
        for c in self.customers:
            if c.customer_id == customer_id:
                customer=c
                break
        
        #If customer not found
        if not customer:
             print('Customer not found')
             return
            
        #If no vehicle rented
        if not customer.rented_vehicle:
             print('this customer has not rented any vehicle. ')
             return
        #return vehicle
        vehicle = customer.rented_vehicle
        vehicle.return_vehicle()
        customer.return_vehicle()
        print('Vehicle returned Successfully by',customer.name)

    def view_customer_details(self):
        for c in self.customers:
            print('customer id :',c.customer_id)
            print('Name :',c.name)
            c.view_rented_vehicle()
            