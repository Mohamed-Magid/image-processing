# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import data from scikit-image library
from skimage import data
# import exposure from scikit-image library
from skimage import exposure
image = data.camera()
equalization = exposure.equalize_hist(image)
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
# display image after equalization
plt.imshow(equalization, cmap= 'gray' )
# put title for image
plt.title( 'after equalization' )
# show image
plt.show()
# display histogram equalization
plt.hist(equalization.ravel())
# put title for image
plt.title( 'histogram equalization' )
# show image
plt.show()