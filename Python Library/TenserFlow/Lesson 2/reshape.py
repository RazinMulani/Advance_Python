# tf.reshape(): Change the shape (dimensions) of a tensor without changing data
# Important: tf.reshape() changes only the structure, not the values stored in the tensor.

# Syntax: tf.reshape(Tensor, shape)
# Parameter	     Meaning
# tensor	- The tensor to reshape
# shape	        - New desired shape

# Example 1: Reshape 1-D to 2-D
import tensorflow as tf
print("=========================Example 1: Reshape 1-D to 2-D====================")

v1 = tf.constant([1,2,3,4,5,6])
print(v1)
print("\nShape: ",v1.shape)

reshape = tf.reshape(v1, (2,3))
print(reshape)
print("\nShape: ",reshape.shape)

print("=========================Example 2: Reshape 2-D to 3-D====================")

v2 = tf.constant([
    [1,2,3],
    [4,5,6]
])

res = tf.reshape(v2, (3,2))
print(res)

print("=========================Example 3: Reshape 3-D====================")
v3 = tf.constant([1,2,3,4,5,6,7,8])

res1 = tf.reshape(v3, (2,2,2))
print(res1)

# Using -1 in Reshape
print("=========================Example 4: Using -1 in Reshape====================")
v4 = tf.constant([1,2,3,4,5,6])
res2 = tf.reshape(v4, (2,-1))
print(res2)

# Complete Example
print("=========================Example 4: Complete Example====================")

x = tf.constant([1,2,3,4,5,6])

print("Original Shape:", x.shape)

y = tf.reshape(x, (2,3))

print("New Shape:", y.shape)

print(y)
