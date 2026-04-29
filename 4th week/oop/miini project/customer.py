class Customer :
    def __init__(self,customer_id,name):
        self.customer_id= customer_id
        self.name= name
        self.rented_vehicle= None
    
    def rent_vehicle(self,vehicle):
        
        self.rented_vehicle= vehicle
    
    def return_vehicle(self):
        self.rented_vehicle = None
        
    def view_rented_vehicle(self):
        if self.rented_vehicle:
            print('customer :',self.name)
            print('Rented vehicle :',self.rented_vehicle.model)
        else:
            print('No vehicle is rented. :')