# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import data from scikit-image library
from skimage import data
image = data.camera()
# display image
# pass image to pyplot to show it later
plt.imshow(image, cmap= 'gray' )
# put title for image
plt.title( 'gray' )
# show image
plt.show()
# display histogram
plt.hist(image.ravel())
# put title for image
plt.title( 'histogram' )
# show image
plt.show()