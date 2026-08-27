# json_practice.py

import json

student = {
    "std_id":101,
    "std_name":"razin",
    "std_age":22,
    "course":"computer",
    "city":"Pune"
    }
# save dictionary to json file

with open("student.json","w") as file:
    json.dump(student, file, indent=4)

print("Data Save Successfully!")

# Read Data From JSON

with open("student.json","r") as file:
    data = json.load(file)

print("\nData From JSON File:")
print(data)

print("\nStudent Name:", data["std_name"])
print("Student Age:", data["std_age"])
