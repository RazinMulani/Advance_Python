# Defination: A Tensor is a multidimensional array is used to store data in TensorFlow
# Everything Inside The tensorflow Is store In Tensor
# example
import tensorflow as tf
message = tf.constant("Hello TensorFlow")
print(message)

# Types Of TensorFlow:
# 0-D Tensor (Scalar): Only One Value
'''
import tensorflow as tf
x = tf.constant(5)
print("0-D Tensor: ",x)
'''
# 1-D Tensor (vector): multiple values in one array
'''
import tensorflow as tf
x = tf.constant([10,20,30,40])
print("1-D Tensor: ",x)
'''

# 2-D Tensor (matrix): Multiple arrays
'''
import tensorflow as tf
x = tf.constant([
    [1,2],
    [3,4]
    ])

print("2-D Tensor: ",x)
'''

# 3-D Tensor : Multiple Matrix
'''
import tensorflow as tf
x = tf.constant([
    [
        [1,2],
        [3,4]
    ],[
        [5,6],
        [7,8]
    ]
    ])

print("3-D Tensor: ",x)
'''
