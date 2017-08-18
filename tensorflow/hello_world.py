# reference : https://www.tensorflow.org/get_started/get_started
import tensorflow as tf

# prints Hello World! on console
hello = tf.constant('Hello World!')
sess = tf.Session()
print(sess.run(hello))
