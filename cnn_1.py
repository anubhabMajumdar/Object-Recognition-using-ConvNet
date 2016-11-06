import tensorflow as tf
import read_data_multiple_category as read_data
import time

CATEGORIES = ["003.backpack", "012.binoculars", "062.eiffel-tower", "078.fried-egg"]
START_STOP_LIST = [[0, 130], [0, 195], [0, 62], [0, 89]]
SIZE = 28

# read data
train_data = read_data.read_data_multiple_category(START_STOP_LIST, CATEGORIES, SIZE)
print "Finished reading data"
print "Training set size =", len(train_data)

