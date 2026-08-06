# tf.ones(): Creates a Tensor Fields With Ones(tf.ones())
# It is commonly used to initialize tensors, create masks, or prepare input data for machine learning
# models.
# Syntax: tf.ones(shape, dtype=tf.flaot32)

# Example: Create 1-D Tensor
import tensorflow as tf
print("==================Example 1: Create 1-D Tensor=================")

v1 = tf.ones((5))
print(v1)

# Example 2: Create 2X3 Tensor
print("\n==================Example 1: Create 2x3 Tensor=================")

v2 = tf.ones((2,3))
print(v2)

# Example 3: Create 3X4 Tensor
print("\n==================Example 1: Create 3x4 Tensor=================")

v3 = tf.ones((3,4))
print(v3)

# Example 4: Create 3-D Tensor
print("\n==================Example 1: Create 3-D Tensor=================")

v4 = tf.ones((2,2,3))
print(v4)

# Change The Data Types
print("\n==================Change The Data Types=================")
# Bydefault data type is float32

print("\n==================Change The Data Types float32 into int32=================")

v5 = tf.ones((2,2),dtype=tf.int32)
print(v5)

print("\n==================Change The Data Types float32 into bool=================")

v6 = tf.ones((3,4,4),dtype=tf.bool)
print(v6)

# Complete Example:
print("\n==================Complete Example=================")

a = tf.ones((3,2),dtype=tf.bool)
print("Tensor:")
print(a)

print("\nShape: ",a.shape)
print("Dtype: ",a.dtype)



