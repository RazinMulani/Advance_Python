# tf.zeros(): Creates a tensor of a specified shape where every element is 0.
# It is useful when you need an initial Tensor filled with zeros before performing calculation or training
# a machine learning model.
# Syntax: tf.zeros(shape, dtype=tf.float32)

# Example: 0-D Tensor
import tensorflow as tf

print("=====================Example1: 0-D Tensor====================")
v1 = tf.zeros(())
print(v1)

print("\n=====================Example1: 1-D Tensor====================")
v2 = tf.zeros((3))
print(v2)

print("\n=====================Example1: 2-D Tensor====================")
v3 = tf.zeros((2,2))
print(v3)

print("\n=====================Example1: 3-D Tensor====================")
v4 = tf.zeros((2,2,2))
print(v4)

print("\n=====================Example1: Create a 2 × 3 Tensor====================")
v5 = tf.zeros((2,3))
print(v5)

print("\n=====================Example1: Create a 3 × 4 Tensor====================")
v6 = tf.zeros((3,4))
print(v6)

print("=====================Example1: Create a 3-D Tensor====================")
v7 = tf.zeros((2,2,3))
print(v7)
# 2 Blocks
# Each block has 2 Rows
# Each row has 3 Columns

print("=====================Changing The Data Types====================")
# Bydefault Data type is Float32
print("\n=====================Changing The Data Type Float32 into Int32====================")
v8 = tf.zeros((3,3),dtype=tf.int32)
print(v8)

print("\n=====================Changing The Data Type Float32 into bool====================")
v9 = tf.zeros((4,5),dtype=tf.bool)
print(v9)

print("\n=====================Complete Example====================")
a = tf.zeros((2,2),dtype=tf.int32)

print("Tensor:\n")
print(a)

print("\nShape: ",a.shape)
print("Dtype: ",a.dtype)


