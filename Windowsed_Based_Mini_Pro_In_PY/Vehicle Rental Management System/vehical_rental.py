# Vehicle Rental Management System

class Vehicle:
    def __init__(self,vehicle_id, vehicle_name, vehicle_type, model, rent_per_day, availability):
        self.v_id = vehicle_id
        self.v_name = vehicle_name
        self.v_type = vehicle_type
        self.v_model = model
        self.v_rent_per_day = rent_per_day
        self.v_availability = availability
    def display(self):
        print("Vehicle ID: ",self.v_id)
        print("Vehicle Name: ",self.v_name)
        print("Vehicle Type: ",self.v_type)
        print("Vehicle Model: ",self.v_model)
        print("Vehicle rent_per_day: ",self.v_rent_per_day)
        print("Vehicle availability: ",self.v_availability)
'''
mustang = Vehicle("V001","Ford Mustang Gt","Sport Car","2024",15000,"Available")
fortuner = Vehicle("V002","Toyota Fortuner","SUV","2024",8000,"Available")
bmw = Vehicle("V003","BMW M4","Sport Car","2024",18000,"Available")

vehicles = [mustang, fortuner, bmw]
'''
vehicles = []
def add_vehicle():
    vehical_id = input("Enter Vahicle ID: ")
    vehical_name = input("Entere Vehicle Name: ")
    vehical_type = input("Enter Vehicle Type: ")
    model = input("Enter Vehicle Model: ")
    rent_per_day = int(input("Enter Rent Per Day: "))
    print("Vehical Is Available")

add_vehicle()

for vehicle in vehicles:
    vehicle.add_vehicle()


