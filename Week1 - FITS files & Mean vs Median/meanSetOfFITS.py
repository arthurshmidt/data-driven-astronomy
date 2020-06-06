# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def mean_fits(data_files):
  data_hold=[]
  counter=0
  for data_file in data_files:
    counter+=1
    hdulist = fits.open(data_file)
    data = hdulist[0].data
    if counter > 1:
      data_hold=data_hold+data
    else:
      data_hold=data
  return data_hold/counter

def load_fits(data_file):
  hdulist = fits.open(data_file)
  data = hdulist[0].data
  max_val = np.unravel_index(np.argmax(data),data.shape)
#  print(data.shape)

  return max_val

def mean_datasets(data_files):
  data_hold=[]
  counter=0
  for data_file in data_files:
    counter+=1
    data = np.loadtxt(data_file, delimiter=',')
    if counter > 1:
      data_hold=data_hold+data
    else:
      data_hold=data
#    print(np.around(data_hold/counter,1))
  return np.around(data_hold/counter,1)


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  pulse_image = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
  average_fits = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])[100,100]
  print(average_fits)
  # bright = load_fits('image2.fits')
  # print(bright)

  # You can also confirm your result visually:
  #hdulist = fits.open('image1.fits')
  #data = hdulist[0].data
  # Arthur Testing
  # hdulist.info()
  # print(data.shape)
  # print(len(hdulist))

  # Plot the 2D image data
  '''
  plt.imshow(pulse_image.T, cmap=plt.cm.viridis)
  plt.xlabel('x-pixels (RA)')
  plt.ylabel('y-pixels (Dec)')
  plt.colorbar()
  plt.show()
  '''
