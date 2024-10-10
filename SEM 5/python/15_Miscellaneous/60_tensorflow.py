import tensorflow as tf

a = tf.constant(5)
b = tf.constant(3)

c_add = tf.add(a, b)
c_subtract = tf.subtract(a, b)
c_multiply = tf.multiply(a, b)
c_divide = tf.divide(a, b)

print("a + b =", c_add.numpy())
print("a - b =", c_subtract.numpy())
print("a * b =", c_multiply.numpy())
print("a / b =", c_divide.numpy())

list_a = tf.constant([1, 2, 3, 4])
list_b = tf.constant([5, 6, 7, 8])

c_list_add = tf.add(list_a, list_b)
c_list_multiply = tf.multiply(list_a, list_b)

print("List a + List b =", c_list_add.numpy())
print("List a * List b =", c_list_multiply.numpy())

matrix_a = tf.constant([[1, 2], [3, 4]])
matrix_b = tf.constant([[5, 6], [7, 8]])
c_matrix_multiply = tf.matmul(matrix_a, matrix_b)

print("Matrix A:\n", matrix_a.numpy())
print("Matrix B:\n", matrix_b.numpy())
print("Matrix A * Matrix B:\n", c_matrix_multiply.numpy())
