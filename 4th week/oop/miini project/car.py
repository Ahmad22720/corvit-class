 
from vehicle import Vehicle
 #car class (inheritance classes)

class Car(Vehicle):
    def __init__(self,vehicle_id,brand,model,price,num_doors,fuel_type):
        super().__init__(vehicle_id,brand,model,price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    def display_info(self):
        super().display_info()
        print('Doors  :',self.num_doors)
        print('Fuel Type :',self.fuel_type)
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day*days
    

