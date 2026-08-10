# WAP python to desplay file information
'''
f = open("razin.txt","w")
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is File Readable: ",f.readable())
print("Is File Writaable: ",f.writable())
print("Is Closed: ",f.closed)
f.close()
print("Is File Is Colsed: ",f.closed)
'''
# Writing Data To Text File
# write(str)
'''
f = open("razin.txt","w")
f.write("Hello\n")
f.write("I'm Razin\n")
f.write("I'm From Mahableshwar")
f.close()
'''
# Writeline(list of lines)
'''
f =open("razin.txt","w")
list = ["Razin\n","Rafik\n","Mulani\n","Sami"]
f.writelines(list)
print("List Of Lines Written In The File")
f.close()
'''

# Reading Character Data From Text File:-
# read() --> Read Total Data From The File
# read(n) --> Read n Character From The File
# readlie() --> Read Only One Lines
# readlines() --> Read All Lines Into List

# WAP to read total data from a file?
'''f = open("razin.txt","r")
data = f.read()
print(data)
f.close()'''
# WAP to read Number(n) Of Characters from a file?
'''f = open("razin.txt","r")
data = f.read(15)
print(data)
f.close()'''

# WAP to read data Line By Line from a file?
'''
f = open("razin.txt","r")
data = f.readline()
print(data)
data1 = f.readline()
print(data1)
f.close()
'''

# WAP to readable total data from a file?
'''
f = open("razin.txt","r")
data = f.readlines()
for x in data:
    print(x)
f.close()
'''

# With Statements:
'''
with open("razin.txt","w") as f:
    f.write("Razin\n")
    f.write("Software\n")
    print("(Inside BlocK)Is File Closed:",f.closed)
print("(Otside The Block)File Closed:",f.closed)
'''

# Seek and Tell() Method:

# Tell()
'''
f = open("razin.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(5))
'''
# Seek()
'''
f = open("razin.txt","r")
f.seek(0)
text = f.read()
print(text) # o/p: Razin Mulani
'''





    
