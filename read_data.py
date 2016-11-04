import os
import glob
from SimpleCV import *

print __doc__

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

	for file in files[start:stop+1]:
	        new_img = Image(file)
	        
	        if g:
	        	grey = new_img.greyscale()
	        else:
	        	grey = new_img	
	        
	        grey = grey.resize(size, size)
	        out.append(grey)
	        #grey.show()
	        #time.sleep(1) #wait for 1 second

	return out        


# Use case
#out = read_data(0, 9)

