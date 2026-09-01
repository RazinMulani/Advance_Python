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


# Practice of Multilevel inheritance

class GrandFather:
    def house(self,name,flat_gf,loc,rate,sqr):
        self.gf_name=name
        self.grandfather_flat = flat_gf
        self.location=loc
        self.rate_house=rate
        self.square_feet=sqr
        
    def display_1(self):
        print("Grand Fahter has a house")
        print("grand father name",self.gf_name)
        print("Grand Father Flat Name:",self.grandfather_flat)
        print("house location:",self.location)
        print("house rate:",self.rate_house)
        print("house square_feet",self.square_feet)
        
        

class Father(GrandFather):
    def car(self,c_name,model,colour,fuel_type,car_type):
        self.car_name = c_name
        self.car_model=model
        self.car_colour=colour
        self.c_fuel=fuel_type
        self.c_type=car_type
    def display_2(self):
        print("Father Has a Car")
        print("Father Car Name: ",self.car_name)
        print("car model",self.car_model)
        print("car colour",self.car_colour)
        print("fuel type of car",self.c_fuel)
        print("type of car",self.c_type)
        

class Son(Father):
    def bike(self,b_name,b_model, b_colur,b_type):
        self.bike_name = b_name
        self.bike_model = b_model
        self.bike_colur = b_colur
        self.bike_type = b_type
    def display_3(self):
        print("Son Has A Bike")
        print("Bike Name:",self.bike_name)
        print("Bike Model:",self.bike_model)
        print("Bike colur:",self.bike_colur)
        print("Bike Type:",self.bike_type)
        

o = Son()
o.house("moahmmed","Shanti Nivas","pune",100000,"720sqr")
o.display_1()
o.car("Mustang",2010,"red","diesel","sport car")
o.display_2()
o.bike("Activa",2017,"White","City Bike")
o.display_3()

# Example Of Multiple Inheritance

# Q. Create a Python program for a Student Result System using Multiple Inheritance.

class Student:
    def display_1(self):
        print("Student Name:",self.std_name)
        print("Student Father Name:",self.std_father)
        print("Student Roll No:",self.roll_no)
        print("Student Age:",self.std_age)
        print("Student Subject:",self.std_gender)
        

class Marks:
    def display_2(self):
        print("Python Marks of Student is: ",self.py_marks)
        print("SQL Marks of Student is: ",self.sql_marks)
        print("Java Marks Of Student is: ",self.java_marks)
        print("C Marks of Student is:",self.c_marks)
        print("PHP Marks Of Student is: ", self.php_marks)

class Result(Student, Marks):
    def display_3(self):
        self.total = self.py_marks + self.sql_marks + self.java_marks + self.c_marks + self.php_marks
        print("Total Mark of Student is:",self.total)

obj = Result()
obj.std_name = "Razin"
obj.std_father = "Rafik"
obj.roll_no = 101
obj.std_age = 22
obj.std_gender = "Male"
obj.py_marks = 56
obj.sql_marks = 78
obj.java_marks = 90
obj.c_marks = 45
obj.php_marks = 67
obj.display_1()
obj.display_2()
obj.display_3()


# Using Cunstructor

class Student:
    def __init__(self,std_n, std_r_n, std_age,std_streem, std_gender, **kwargs):
        super().__init__(**kwargs)
        self.name = std_n
        self.roll_no = std_r_n
        self.age = std_age
        self.streem = std_streem
        self.gender = std_gender

class Marks:
    def __init__(self,py_marks,sql_marks,java_marks,c_marks,html_marks, **kwargs):
        super().__init__(**kwargs)
        self.python = py_marks
        self.sql = sql_marks
        self.java = java_marks
        self.c = c_marks
        self.html = html_marks

class Result(Student,Marks):
    def __init__(self,std_n,std_r_n,std_age,std_streem,std_gender,py_marks,sql_marks,java_marks,c_marks,html_marks):
        super().__init__(
            std_n = std_n,
            std_r_n = std_r_n,
            std_age = std_age,
            std_streem = std_streem,
            std_gender = std_gender,
            py_marks = py_marks,
            sql_marks = sql_marks,
            java_marks = java_marks,
            c_marks = c_marks,
            html_marks = html_marks
            )


    def display(self):
        print("Student Name:",self.name)
        print("Student Roll No.:",self.roll_no)
        print("Student Age:",self.age)
        print("Student Streem:",self.streem)
        print("Student Gender:",self.gender)
    
        print("Python Marks:",self.python)
        print("SQL Marks:",self.sql)
        print("JAVA Marks:",self.java)
        print("C Marks:",self.c)
        print("HTML Marks:",self.html)
        
        total = self.python + self.sql + self.java + self.c + self.html
        print("Total Marks:",total)



obj1 = Result("Razin",101,22,"CS","Male",56,78,67,89,70)
obj1.display()


# 📝 Practice Question: Employee Management System
# Create a Python program using Hybrid Inheritance for an Employee Management System.

class Person:
    def person_info(self,p_n,p_a):
        self.name = p_n
        self.age = p_a

    def display_1(self):
        print("Name of Person:",self.name)
        print("Age of Person:",self.age)

class Employee(Person):
    def employee_info(self,emp_id,emp_d):
        self.employee_id = emp_id
        self.employee_d = emp_d

    def display_2(self):
        print("Employee ID:",self.employee_id)
        print("Employee Department:",self.employee_d)

class Salary:
    def salary_info(self,b_salary,s_b):
        self.basic_salary = b_salary
        self.bonus = s_b

    def display_3(self):
        print("Basic Salary:",self.basic_salary)
        print("Bonus:",self.bonus)

class Manager(Employee,Salary):
    def total(self):
        total = self.basic_salary + self.bonus
        print("Total:",total)



o = Manager()
o.person_info("Razin",22)
o.display_1()
o.employee_info("E101","IT")
o.display_2()
o.salary_info(1000000,20000)
o.display_3()
o.total()


# 📝 Practice Question: Vehicle Management System
# Create a Python program using Hierarchical Inheritance.

class Vehicle:
    def vehicle_info(self,v_n,v_t,r_p_d):
        self.vehicle_name = v_n
        self.vehicle_type = v_t
        self.vehicle_rent_p_d = r_p_d

        print("Vehicle Name:",self.vehicle_name)
        print("Vehicle Type:",self.vehicle_type)
        print("Vehicle Rent Per Day:",self.vehicle_rent_p_d)

class Car(Vehicle):
    def car_info(self,n_o_d):
        self.number_of_door = n_o_d

        print("Number Of Door in Car:",self.number_of_door)


class Bike(Vehicle):
    def bike_info(self,e_cc):
        self.engine_cc = e_cc

        print("Engine CC:",self.engine_cc)



o = Car()
o.vehicle_info("BMW","Sport Car",120000)
o.car_info(4)

o1 = Bike()
o1.vehicle_info("Royal Enfield Classic 350","Bike",20000)
o1.bike_info(350)


