# Tensor Shape
# What is Shape in Tensor?
# Tensor Shape Tells us The Structrue of a tensor, including: Number of dimension, number of rows, number
# of columns, and size of each dimension
# in simple words, tensor describe how data is aaranged in inside a Tensor.

# Syntax: tensor.shape
# 1) 0-D Tensor(Scalar)
import tensorflow as tf
print("0-D Tensor(Scalar)")
x=tf.constant(10)
print(x)
print(x.shape)

# 2) 1-D Tensor(Vector)
print("\n1-D Tensor(Vector)")
v1 = tf.constant([10,20,30])
print(v1)
print(v1.shape)

# 3) 2-D Tensor(Matrix)
print("\n2-D Tensor(Matrix)")
v2 = tf.constant([[10,20],[30,40]])
print(v2)
print(v2.shape)

# 4) 3-D Tensor(Nested Matrix)
print("\n3-D Tensor(Nested Matrix)")
v3 = tf.constant([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
    ])
print(v3)
print(v3.shape)
