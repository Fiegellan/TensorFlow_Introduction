import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

#results = x1*x2

results = tf.mul(x1,x2)

print(results)

with tf.Session() as sess:
	ouput = ses.run(results))
	print(output)