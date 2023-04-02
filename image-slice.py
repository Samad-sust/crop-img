# Import the libraries
import image_slicer
import glob

# the directory of the images to be open 
main_image_dir = "/home/samad/Desktop/Images/squared"

# the directory of the images to be saved after cropping
sliced_image_dir = "/home/samad/Desktop/Images/sliced"

# listing the contents of the directory
contents_in_dir = glob.glob( main_image_dir + '/*.jpg')

# total images to be produced after cropping
# a full squared rooting number such as 4,9,16,15 devides an image evenli through width and height
no_of_slice = 16

# crop every images of the directory mentioned above
for image in contents_in_dir:
    image_slicer.slice(image, no_of_slice)
