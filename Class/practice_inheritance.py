# Practice of Single Inheritance
# Question: Create a Python program using single inheritance for a Vehicle Rental System.
# Requirements:
# Create a parent class Vehicle with:
# vehicle_name
# vehicle_type
# rent_per_day
# Create a child class RentalVehicle that inherits from Vehicle and adds:
# rental_days
# Add a method calculate_rent() in the child class to calculate:
# Total Rent = rent_per_day × rental_days

class Vehicle:
    def set_vehicle(self,v_name,v_type,r_p_d):
        self.vehicle_name = v_name
        self.vehicle_type = v_type
        self.rent_per_day = r_p_d


    def display_1(self):
        print("Vehicle Name:",self.vehicle_name)
        print("Vehicle Type:",self.vehicle_type)
        print("Rent Per Day:",self.rent_per_day)

class RentalVehical(Vehicle):
    def set_rental(self,r_days):
        self.rental_days = r_days

    def display_2(self):
        print("Rental Days:",self.rental_days)
        total_rent = self.rent_per_day * self.rental_days
        print("Result:",total_rent)
        
# input From User
v_name = input("Enter Car Name:")
v_type = input("Enter Vehicle Type:")
r_p_d = int(input("Enter Rent:"))

r_days = int(input("Enter Days:"))
o = RentalVehical()
o.set_vehicle(v_name,v_type,r_p_d)
o.set_rental(r_days)
o.display_1()
o.display_2()
