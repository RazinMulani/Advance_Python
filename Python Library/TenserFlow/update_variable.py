# Update Variable: A Variable stores a value that can change.
# Method 1: assign() replace the old value with a new value
# Syentax: Variable.assign(new_value)

# Example:
'''
import tensorflow as tf

x = tf.Variable(10)

print("Old Value: ",x)

x.assign(100)
print("\nUpdated Value: ",x)
'''

# Method 2: assign() Adds  a Value to The Current Variable
# Syntax: variable.assign_add(value)

#Example:
'''
import tensorflow as tf

x = tf.Variable(100)
print("Before: ",x)

x.assign_add(50)

print("After: ",x)
'''

# Method 3: assign_sub() Substract a Value To The Current Variable
# Syntax: Variable.assign_sub(value)

# Example:
'''
import tensorflow as tf

x = tf.Variable(100)
print("Before: ",x)
x.assign_sub(50)
print("\nAfter: ",x)
'''

# WAP To update, add and Sub value in one frame

import tensorflow as tf

x = tf.Variable(4857)
print("OG Value: ",x.numpy())  # o/p: 4857

# Update Value
update_value = x.assign(5000)
print("\nUpdated Value: ", x.numpy()) #o/p: 5000

# Added 3000 in x variable
add_value = x.assign_add(3000)
print("\nAdded 3000 in OG Value: ",x.numpy()) #o/p: 5000+3000 = 8000

# Substract 2000 in x variable
sub_value = x.assign_sub(2000)
print("\nSubstract The Value From Add_value Vaiable: ",add_value.numpy())#o/p: 8000-2000=6000


