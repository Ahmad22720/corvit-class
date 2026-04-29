from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self,vehicle_id,brand,model,price,engine_capacity,bike_type):
        super().__init__(vehicle_id,brand,model,price)
        self.engine_capacity= engine_capacity
        self.bike_type= bike_type
       
    def display_info(self):
        super().display_info()
        print('Engine :',self.engine_capacity)
        print('Type... :',self.bike_type)
        
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day*days

