# Simple computational method

import os
import tensorflow as tf

# Turn off Tensorflow warning message in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational graph
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

addition = tf.add(X, Y, name="addition")

# Tensorflow Session :
# an object that runs operations on the computation graph and tracks the state of each node in the graph
# Create the session
with tf.Session() as session:
    result = session.run(addition, feed_dict={X: [2, 1, 9], Y: [5, 90, 25]})
    print(result)
