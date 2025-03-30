import tensorflow as tf
hello=tf.constant("hello world")
output=hello.numpy()
print(output.decode())