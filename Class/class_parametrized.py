# Parametraized Method In Class
'''
class student:
    def __init__(self,r,n,a):
        self.roll = r
        self.name = n
        self.age = a
    def display(self):
        print("My Roll No Is: ",self.roll)
        print("My Name Is: ",self.name)
        print("My Age Is: ",self.age)
        
s = student(101,"Razin",22)
s.display()
s1 = student(102,"Sami",20)
s1.display()
'''

# Q.
'''
class owner_property:
    def __init__(self,o_no,o_n,o_a,pn,pna,pl,pr,psq):
        self.o_number=o_no
        self.name=o_n
        self.adrr=o_a
        self.p_no=pn
        self.p_name=pna
        self.p_loc=pl
        self.p_rate=pr
        self.p_sqr=psq
        
    def display(self):
        print("Owner No = ",self.o_number)
        print("Owner Name = ",self.name)
        print("Owner Adress = ",self.adrr)
        print("Owner Plot No = ",self.p_no)
        print("Owner Plot Name = ",self.p_name)
        print("Owner Plot Location = ",self.p_loc)
        print("Owner Plot Rate = ",self.p_rate)
        print("Owner Plot Squarefit = ",self.p_sqr)
        
o1 = owner_property(9404813157,"Razin","Pune",101,"xyz","Mumbai",100000,200000)
o2 = owner_property(9404813157,"Sami","Pune",102,"xyz1","Kolkata",200000,200000)
o3 = owner_property(9404813157,"Asjad","Pune",103,"xyz2","Madras",300000,200000)
o1.display()
o2.display()
o3.display()
'''
# Q. Get input from user:

class owner_property:
    def __init__(self,o_no,o_n,o_a,pn,pna,pl,pr,psq):
        self.o_number=o_no
        self.name=o_n
        self.adrr=o_a
        self.p_no=pn
        self.p_name=pna
        self.p_loc=pl
        self.p_rate=pr
        self.p_sqr=psq
        
    def display(self):
        print("Owner No = ",self.o_number)
        print("Owner Name = ",self.name)
        print("Owner Adress = ",self.adrr)
        print("Owner Plot No = ",self.p_no)
        print("Owner Plot Name = ",self.p_name)
        print("Owner Plot Location = ",self.p_loc)
        print("Owner Plot Rate = ",self.p_rate)
        print("Owner Plot Squarefit = ",self.p_sqr)

# Take input From User:
o_no = int(input("Enter Owner Number:"))
o_n = input("Enter Owner Name:")
o_a = input("Enter Owner Address:")
pn = int(input("Emter Property Number: "))
pna = input("Enter Property name:")
pl = input("Enter Property Location:")
pr = int(input("Enter Property Rate:"))
psq = int(input("Enter Property Squarefoot:"))

o_no1 = int(input("Enter Owner Number:"))
o_n1 = input("Enter Owner Name:")
o_a1 = input("Enter Owner Address:")
pn1 = int(input("Emter Property Number: "))
pna1 = input("Enter Property name:")
pl1 = input("Enter Property Location:")
pr1 = int(input("Enter Property Rate:"))
psq1 = int(input("Enter Property Squarefoot:"))

o_no2 = int(input("Enter Owner Number:"))
o_n2 = input("Enter Owner Name:")
o_a2 = input("Enter Owner Address:")
pn2 = int(input("Emter Property Number: "))
pna2 = input("Enter Property name:")
pl2 = input("Enter Property Location:")
pr2 = int(input("Enter Property Rate:"))
psq2 = int(input("Enter Property Squarefoot:"))

        
o1 = owner_property(o_no,o_n,o_a,pn,pna,pl,pr,psq)
o2 = owner_property(o_no1,o_n1,o_a1,pn1,pna1,pl1,pr1,psq1)
o3 = owner_property(o_no2,o_n2,o_a2,pn2,pna2,pl2,pr2,psq2)
o1.display()
o2.display()
o3.display()
