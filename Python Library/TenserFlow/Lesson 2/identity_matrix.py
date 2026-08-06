# tf.eye(): Am identity matrix in a square matrx in which:
# --> All digonal elemnts are 1
# --> All other elemnts are 0
# Syntax: tf.eye(
#                num_rows,
#                num_columns=None,
#                dtype=tf.float32
#                )

import tensorflow as tf
print("======================Example 1: 3 × 3 Identity Matrix====================")

v1 = tf.eye((3))
print(v1)

print("\n======================Example 2: 4 × 4 Identity Matrix====================")

v2 = tf.eye((4))
print(v2)

print("\n======================Example 3: 4 × 6 Identity Matrix====================")
# note: get num_rows seprate intiger
v3 = tf.eye(4,6)
print(v3)

print("\n======================Example 4: Change DType into int Identity Matrix====================")

v4 = tf.eye((2), dtype=tf.int32)
print(v4)

print("\n======================Example 5: Change DType into bool Identity Matrix====================")

v5 = tf.eye((3),dtype=tf.bool)
print(v5)

# Example 4: Rectangular Identity Matrix
print("\n======================Example 6: Rectangular Identity Matrix====================")

v6 = tf.eye(
    num_rows = 3,
    num_columns = 5
    )
print(v6)

# Complete Example
import tensorflow as tf
print("\n======================Example 6: Complete Example ====================")

matrix = tf.eye(4)

print("Identity Matrix")
print(matrix)

print("Shape:", matrix.shape)

print("Data Type:", matrix.dtype)
