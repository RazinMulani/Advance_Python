# Practice: Lesson 2
import tensorflow as tf
print("Print Variable")
a = tf.Variable(50)
print("Original:",a)

print("\nAddition With Variable")
a.assign_add(25)
print("After Addition:",a)

print("\nGet only Zeros")
zeros = tf.zeros((2,2))
print(zeros)

print("\nGet Only Ones")
ones = tf.ones((3,2))
print(ones)

print("\nPrint The Matrix")
matrix = tf.reshape(
    tf.constant([1,2,3,4]),
    (2,2)
    )

print(matrix)
