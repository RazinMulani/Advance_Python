# SCIPY MODULS:
#Module	         #Purpose
#scipy.constants Mathematical and physical constants
# is module in the scipy library that provides predefined mathamaticcal, Physical, and scintific
# constant with high precision
'''
from scipy import constants

# Mathamatical Constant
print("\nMathamatical Constant\n")
print("pi=",constants.pi) # pi is the ratio of a circle sircumference  to its diameter.
print("Euler's=",constants.e) #euler's number is based on the natural algorithem 
print("Golden Ratio=",constants.golden)# the goldan ratio is mathamatically constant approximatly equal to 1.618

# Physical Constant
print("\nPhysical Constant\n")
print("Speed Of Light=",constants.c) # speed of light in a vacum
print("Gravitational_acc=",constants.g) # The standard acceleration due to Earth's gravity.
print("Gravitational_cons=",constants.G) # The universal gravitaional constantsused in newton's low of gravity

# Chemistry Constants
print("\nChemistry Constants\n")
print("Avogadro Const=",constants.Avogadro) # The numbers of Particals (atoms, molecules, or ions) present in one of a substance
print("Boltzman Const=",constants.Boltzmann) # Relates the average kinetic energy of particles in a gas to temperature.
'''
# Example Of Constant
# Q. find The area of circule(pir*r^2)
'''
from scipy import constants

radius = int(input("Enter The value of Radius: "))

result= constants.pi * radius ** 2
print("Aria Of Circule Is: ",result)
'''

# Q2. Calculate the circumference of a circle.(2*pi*r)
'''
from scipy import constants
r = int(input("Enter The Value Of Radious: "))
result=2 * constants.pi * r
print("Cicumference of Circule Is: ",result)
'''

