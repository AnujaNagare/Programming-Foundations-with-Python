# reference
import tensorflow as tf

# # prints Hello World! on console
# hello = tf.constant('Hello World!')
# sess = tf.Session()
# print(sess.run(hello))
# print(type(hello))
# print(type(sess))

# create  two floating point Tensors node1 and node2
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)

# To actually evaluate the nodes: run the computational graph within a session
sess = tf.Session() # creates a Session object
# print(sess.run([node1, node2])) # invokes its run method to run enough of the computational graph to evaluate node1 and node2


# combining Tensor nodes with operations
node3 = tf.add(node1, node2) # add node1 and node2
# print("node3: ", node3)
# print("sess.run(node3): ",sess.run(node3))

# A graph can be parameterized to accept external inputs, known as placeholders.
#  function or a lambda in which we define two input parameters (a and b) and then an operation on them
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)

print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))
