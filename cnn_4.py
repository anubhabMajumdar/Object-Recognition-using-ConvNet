import tensorflow as tf
import read_data_multiple_category as read_data
import time
import numpy as np
import random

CATEGORIES = ["003.backpack", "012.binoculars", "062.eiffel-tower", "078.fried-egg"]
START_STOP_LIST = [[1, 131], [1, 196], [1, 63], [1, 70]]
START_STOP_LIST_TEST = [[132, 151], [197, 216], [64, 83], [71, 90]]
SIZE = 64
TOTAL_TRAIN = 0
BATCH = 20
AUGMENT = 8
for i in START_STOP_LIST:
	TOTAL_TRAIN = TOTAL_TRAIN + (i[1] - i[0] + 1)

TRAIN_INDICES = range(AUGMENT*TOTAL_TRAIN)

################################### Load data #######################################

# read data
train_data = read_data.read_data_multiple_category(START_STOP_LIST, CATEGORIES, SIZE)
train_label = []
ind = 0
for i in START_STOP_LIST:
	d = i[1] - i[0] + 1
	x = [0,0,0,0]
	x[ind] = 1		
	for j in range(AUGMENT*d):
		train_label.append(x)
	ind = ind + 1

train_data = np.asarray(train_data)
train_label = np.asarray(train_label)	


test_data = read_data.read_data_multiple_category(START_STOP_LIST_TEST, CATEGORIES, SIZE)
test_label = []
ind = 0
for i in START_STOP_LIST_TEST:
	d = i[1] - i[0] + 1
	x = [0,0,0,0]
	x[ind] = 1		
	for j in range(AUGMENT*d):
		test_label.append(x)
	ind = ind + 1

test_data = np.asarray(test_data)
test_label = np.asarray(test_label)	


#print train_data.shape
#print train_label.shape

#print train_data
#print train_label

print "Finished reading data"
print "Training set size =", len(train_data)
print "Training set size =", len(train_label)
print "Training set size =", len(test_data)
print "Training set size =", len(test_label)

############################################# Session #######################################
#config = tf.ConfigProto(log_device_placement=False)
#config.gpu_options.allow_growth = True

#sess = tf.InteractiveSession(config=config)
sess = tf.InteractiveSession()

########################### Placeholder for inp/out ######################################

x = tf.placeholder(tf.float32, shape=[None, SIZE*SIZE])	# 28x28 image size
y_ = tf.placeholder(tf.float32, shape=[None, 4])	# 4 output class

################################### Weights ######################################

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

################################### Convolution Layer ######################################

def conv2d(x, W, s=1):	#	s -> strides
  return tf.nn.conv2d(x, W, strides=[1, s, s, 1], padding='SAME')

################################### Pooling Layer ######################################

def max_pool(x, size=2, stride=2):
  return tf.nn.max_pool(x, ksize=[1, size, size, 1], strides=[1, stride, stride, 1], padding='SAME')

################################ 1st Convolution Layer #################################

W_conv1 = weight_variable([5, 5, 1, 32])	# computing 64 features (shared weights)
b_conv1 = bias_variable([32])	# 128 shared bias for 32 features

x_image = tf.reshape(x, [-1,SIZE,SIZE,1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool(h_conv1)

################################ 2nd Convolution Layer #################################

W_conv2 = weight_variable([5, 5, 32, 64])	# 128 features in this layer
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool(h_conv2)

################################ 3rd Convolution Layer #################################

W_conv3 = weight_variable([5, 5, 64, 128])	# 128 features in this layer
b_conv3 = bias_variable([128])

h_conv3 = tf.nn.relu(conv2d(h_pool2, W_conv3) + b_conv3)
h_pool3 = max_pool(h_conv3)

################################ Transforming to 1st 1d Layer #################################

W_fc1 = weight_variable([8 * 8 * 128, 512])
b_fc1 = bias_variable([512])

h_pool2_flat = tf.reshape(h_pool3, [-1, 8*8*128])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

################################ Transforming to 2nd 1d Layer #################################

W_fc2 = weight_variable([512, 512])
b_fc2 = bias_variable([512])

h_fc1_transpose = tf.reshape(h_fc1, [-1, 512])
h_fc2 = tf.nn.relu(tf.matmul(h_fc1_transpose, W_fc2) + b_fc2)

############################# Dropout ############################################

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc2, keep_prob)	# prevent overfitting

############################# Output layer ############################################

W_fc2 = weight_variable([512, 4])	# 4 output class
b_fc2 = bias_variable([4])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

############################# Train ############################################

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.initialize_all_variables())
for i in range(10000):
	if i%100 == 0:
  		train_accuracy = accuracy.eval(feed_dict={
        	x:train_data, y_: train_label, keep_prob: 1.0})
    
		print("step %d, training accuracy %g"%(i, train_accuracy))
	
	random.shuffle(TRAIN_INDICES)
	for j in range(0, len(TRAIN_INDICES), BATCH):	
		train_step.run(feed_dict={x: train_data[j:j+BATCH-1], y_: train_label[j:j+BATCH-1], keep_prob: 0.5})
  
############################# Test ############################################

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: test_data, y_: test_label, keep_prob: 1.0}))



