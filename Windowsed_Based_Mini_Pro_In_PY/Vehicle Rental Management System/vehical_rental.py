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
# ============== Add Vehicle ============ #
vehicles = []
def add_vehicle():
    vehicle_id = input("Enter Vehicle ID: ")
    vehicle_name = input("Enter Vehicle Name: ")
    vehicle_type = input("Enter Vehicle Type: ")
    model = input("Enter Vehicle Model: ")
    try:
        rent_per_day = int(input("Enter Rent Per Day: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
        
    availability = "Available"

    vehicle = Vehicle(
        vehicle_id,
        vehicle_name,
        vehicle_type,
        model,
        rent_per_day,
        availability
        )
    vehicles.append(vehicle)
    print("Vehicle Added Successfully!")

# ============== Display Vehicle ============ #
def display_vehicles():
    for vehicle in vehicles:
        vehicle.display()

# ============== Search Vehicle ============ #
def search_vehicle():
    vehicle_id = input("\nEnter Vehicle ID:")
    found = False
    
    for vehicle in vehicles:
        if vehicle.v_id == vehicle_id:
            print("\nVehicle Found\n")

            print("Vehicle ID:",vehicle.v_id)
            print("Vehicle Name:",vehicle.v_name)
            print("Vehicle Type:",vehicle.v_type)
            print("Vehicle Model:",vehicle.v_model)
            print("Vehicle Rent Per Day:",vehicle.v_rent_per_day)
            print("Vehicle Availability:",vehicle.v_availability)
            found = True
            break
        
    if found == False:
        print("Please Enter Valid ID!")

# ============== Delete Vehicle ============ #
def delete_vehicles():
    vehicle_id = input("Enter Vehicle ID to Delete:")
    found = False

    for vehicle in vehicles:
        if vehicle.v_id == vehicle_id:
            print("Vehicle Found!")
            vehicles.remove(vehicle)
            print("Vehicle Deleted Successfully!")
            found = True
            break

    if not found:
        print("Vehicle Not Found!")

# ============== Availability Vehicle ============ #
def availability_vehicle():
    vehicle_id = input("Enter Vehicle ID:")
    found = False

    for vehicle in vehicles:
        if vehicle.v_id ==  vehicle_id:
            print("Found Vehicle Id!")
            print("Vehicle Name:",vehicle.v_name)
            print("Vehicle Availability:",vehicle.v_availability)
            found = True
            break
    if found == False:
        print("Vehicle Not Found!")
        
# ============== Rental Vehicle ============ #
def rent_vehicle():
    vehicle_id = input("Enter Vehicle ID:")
    found = False

    for vehicle in vehicles:
        if vehicle.v_id == vehicle_id:
            print("Vehicle Found!")
            print("Vehicle Name",vehicle.v_name)
            print("Rent Per Day:",vehicle.v_rent_per_day)
            print("Vehicle Availability:",vehicle.v_availability)
            found = True

            if vehicle.v_availability == "Rented":
                print("Vehicle Is Alraedy Rented")
            else:
                rent_days = int(input("Enter Number of Days:"))
                total_rent = vehicle.v_rent_per_day * rent_days
                vehicle.v_availability = "Rented"
                print("Total Rent:",total_rent)
                print("Vehicle Rented successfully!")
            
            break
    if not found:
        print("Vehicle Not Found!")

# ============== Return Vehicle ============ #
def return_vehicle():
    vehicle_id = input("Enter Vehicle ID:")
    found = False

    for vehicle in vehicles:
        if vehicle.v_id == vehicle_id:
            print("Vehicle Found!")
            print("Vehicle Name:",vehicle.v_name)
            print("Vehicle Availability:",vehicle.v_availability)
            found = True

            if vehicle.v_availability == "Rented":
                vehicle.v_availability = "Available"

                print("Vehicle Returned Successfully!")
                print("Vehicle Availability:", vehicle.v_availability)
            else:
                print("Vehicle Is Alrady Available!")
            break

    if not found:
        print("Vehicle Not Found!")
    

while True:
    print("========= Vehicle Rental Management System =========")
    print("1. Add Vehicle")
    print("2. Display Vehicle")
    print("3. Search Vehicle")
    print("4. Delete Vehicle")
    print("5. Check Availability")
    print("6. Rent Vehicle")
    print("7. Return Vehicle")
    print("8. Exit")

    choice = input("\nEnter Your Choice:")

    if choice == "1":
        add_vehicle()
        
    elif choice == "2":
        display_vehicles()
            
    elif choice == "3":
        search_vehicle()

    elif choice =="4":
        delete_vehicle()

    elif choice == "5":
        availability_vehicle()

    elif choice == "6":
        rent_vehicle()

    elif choice == "7":
        return_vehicle()
        
    elif choice == "8":
        print("\nThank you Please Visit Again!")
        break
    
    else:
        print("Please Enter Valid Number!")




