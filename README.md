# Object-Recognition-using-ConvNet
Object recognition using deep ConvNet and Caltch-256 dataset

This project is my first foray in learning and implementing deep convolutional neural network using Tensorflow.

Need python 2.7

Packages
========================
1. TensorFlow
2. Numpy
3. Scipy
4. Matplotlib

Folder
========================
Data -> Contains image data (both test and train)

Files
========================
vcl_setup.sh - Run it to setup tensorflow with GPU support and all important python packages in Ubuntu machine

read_data2.py -> Reads images for given folder and range and augments them using ritation and gaussian blur.

read_data_multiple_category.py -> Wrapper for reading images from multiple folders

cnn_*.py -> Actual CNN network. Initial code is to read the images and create label matrix. Will separate this module out later. cnn_6.py has a provision of stopping the code when the training accuracy flatlines after certein number of iterations.Please use cnn_5.py or cnn_6.py.

To test, just run cnn_6.py. 

# Additional Resources
+ For introduction to Object Recognition and CNN - [projectPaper] 
+ Presentation - [presentation]

# References
* All the references are mentioned in [projectPaper].

   [projectPaper]: <https://drive.google.com/file/d/0BygLf1QZV3ixQlFMRlU1Q2szcVk/view?usp=sharing>
   [presentation]: <https://drive.google.com/file/d/0BygLf1QZV3ixZkhpdjdSMmdsVDA/view?usp=sharing>

