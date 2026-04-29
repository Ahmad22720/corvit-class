# initiate class
class Vehicle:
    # class method
    def __init__(self,vehicle_id,brand,model,rental_price_per_day):
        self.vehicle_id = vehicle_id
        self.brand= brand
        self.model= model
        self.rental_price_per_day= rental_price_per_day
        self.is_available= True

    def display_info(self):
        print("\n ID :",self.vehicle_id)
        print("Brand Name:",self.brand)
        print("model :",self.model)
        print("rental_price_per_day :",self.rental_price_per_day)
        print("Vehicle rental_price_per_day? :",self.is_available)
    
    def rent(self):
        if self.is_available:
            self.is_available= False
            print("Vehicle rented successfully :")
        else:
            print("vehicle is not Available")
            
    def return_vehicle(self):
        self.is_available= True
        print("vehicle is available again :")
        
    def calculate_rental_cost(self,days):
        return self.rental_price_per_day * days