# Variable in TenserFlow
# What is Variable In TensorFlow
# A Variable is a Tensor Whose Value Can be Changed During Program Execution.
# Unlike tf.constant(), a Variable is mutable

import tensorflow as tf

# int
value = tf.Variable(10)
print(value)

# str
v1 = tf.Variable("Razin")
print(v1)

# float
v2 = tf.Variable(10.46)
print(v2)

# Complex
v3 = tf.Variable(3+1j)
print(v3)

# bool
v4 = tf.Variable(True)
print(v4)

# list
#v5 = tf.Variable(["Razin",21,"Pune"]) # tensorflow get only same types of data
v5 = tf.Variable(["Razin","21","Pune"])
print(v5)
# dict
# v6 = tf.Variable({"Name":"Razin","Age":21}) # Tenserflow is not supported dict data type
# print(v6)

# Tuple
v7 = tf.Variable(("Razin","Rafik","Mulani")) # Conver to the list
print(v7)

# set
# v8 = tf.Variable({"Razin","Rafik","Mulani"}) # TensorFlow Is Not Supported set data Type
# print(v8)

# None
# v9 = tf.Variable(None) # not supported
# print(v9)


# Constant Vs Variable
const = tf.constant(10)
var = tf.Variable(10)

print("Constant: ",const)
print("\nVariable: ",var)






















