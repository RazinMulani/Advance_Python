# tf.rendom.normal(): A random  Tensor is a Tensor whose elements are generated randomly insted of being
# fixed values like 0 and 1

# Why do we need? :- ML model start with random weight.
# syntax: tf.random.normal(shape)

# Example: 1-D random Tensor
print("=======================Example: 1-D random Tensor========================")
import tensorflow as tf
v1 = tf.random.normal((5,))

print(v1) # every time number change randomly.

# Example 2: 2 × 3 Random Tensor
print("=======================Example: 2 x 3 random Tensor========================")

v2 = tf.random.normal((2,3))

print(v2)

# Example 3: 3 × 4 Random Tensor
print("=======================Example: 3 x 4 random Tensor========================")
v3 = tf.random.normal((3,4))
print(v3)
# use cast: tf.cast() converts the floating-point values to integers (the decimal part is discarded).
print("\nFloat Into Intiger using tf.cast()")
v3 = tf.cast(v3, tf.int32)
print(v3)

print("\nFloat Into Boolean using tf.cast()")
v3 = tf.cast(v3, tf.bool)
print(v3)

# Example 4: 3-D Random Tensor
print("=======================Example: 3-D random Tensor========================")

v4 = tf.random.normal((2,3,3))
v4 = tf.cast(v4, tf.int32)
print(v4)

# Example 5: Complete Example
print("=======================Example: Complete Example Tensor========================")

v5 = tf.random.normal((2,3))
print(v5)

print("\nShape: ",v5.shape)
print("\nData Type: ",v5.dtype)
