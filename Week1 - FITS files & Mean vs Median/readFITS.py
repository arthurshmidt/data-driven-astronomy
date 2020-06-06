# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(data_file):
  hdulist = fits.open(data_file)
  data = hdulist[0].data
  max_val = np.unravel_index(np.argmax(data),data.shape)
#  print(data.shape)

  return max_val



if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image2.fits')
  print(bright)

  # You can also confirm your result visually:
  #hdulist = fits.open('image1.fits')
  #data = hdulist[0].data
  # Arthur Testing
  # hdulist.info()
  # print(data.shape)
  # print(len(hdulist))

  # Plot the 2D image data
  '''
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.xlabel('x-pixels (RA)')
  plt.ylabel('y-pixels (Dec)')
  plt.colorbar()
  plt.show()
  '''
