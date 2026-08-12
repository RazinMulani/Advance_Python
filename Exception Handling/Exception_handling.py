# Exception Handling Example:
# Q) WAP TO Check Balance if Balance is grater than 1000 display transaction processing else generating
# insufficiant balance
'''
class insuBalance(Exception):
    def __init__(self,arg):
        self.msg = arg

a = int(input("Enter Balance: "))
if(a >= 1000):
    print("Transaction PRocessing!")
else:
    raise insuBalance("Insufficiant Balance")
'''

# Q) WAP Leap Year in Python

try:
    year = int(input("Enter a Year: "))

    if year <= 0:
        raise ValueError("Year Must Be Grater Than '0'")
    elif year % 400 == 0:
        print(year, "Is A Leap Year")
    elif (year % 4 == 0 and year % 100 != 0):
        print(year, "Is A Leap Year")
    else:
        print(year,"Is Not A Leap Year")
        
except ValueError as e:
    print("Invalid Input",e)
