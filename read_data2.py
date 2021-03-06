import os
import glob
import numpy as np
import matplotlib.image as mpimg
from scipy import ndimage
from scipy import misc

def read_data(start, stop, category, size=64, g=True):
	#Settings
	#my_images_path = "data/003.backpack/" #put your image path here if you want to override current directory
	my_images_path = "data/"+category+"/" #put your image path here if you want to override current directory
	extension = "*.jpg"

	#Program
	if not my_images_path:
	        path = os.getcwd() #get the current directory
	else:
	        path = my_images_path

	imgs = list() #load up an image list
	directory = os.path.join(path, extension)
	files = glob.glob(directory)
	out = []

	for file in files[start-1:stop]:
		#image = mpimg.imread(file)
		#image = rgb2gray(image)
		
		image = misc.imread(file, flatten=True)
		image = misc.imresize(image, [size, size])
		image = np.asarray(image)

		temp_img = np.reshape(image, size*size)
		out.append(temp_img)
		#print image.shape

		temp_img = ndimage.gaussian_filter(image, sigma=3)
		temp_img = np.reshape(temp_img, size*size)
		out.append(temp_img)		
		
		image = ndimage.rotate(image, 90)
		temp_img = np.reshape(image, size*size)
		out.append(temp_img)
		
		temp_img = ndimage.gaussian_filter(image, sigma=3)
		temp_img = np.reshape(temp_img, size*size)
		out.append(temp_img)		
		
		image = ndimage.rotate(image, 90)
		temp_img = np.reshape(image, size*size)
		out.append(temp_img)
		
		temp_img = ndimage.gaussian_filter(image, sigma=3)
		temp_img = np.reshape(temp_img, size*size)
		out.append(temp_img)		
				
		image = ndimage.rotate(image, 90)
		temp_img = np.reshape(image, size*size)
		out.append(temp_img)
		
		temp_img = ndimage.gaussian_filter(image, sigma=3)
		temp_img = np.reshape(temp_img, size*size)
		out.append(temp_img)		
				
	out = np.asarray(out)	
	return out


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

# Use case
#out = read_data(1, 151, "003.backpack", 28, False)
#print out.shape
#out[0].show()
#time.sleep(1)
