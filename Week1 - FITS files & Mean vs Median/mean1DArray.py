# Write your calc_stats function here.
import numpy as np

def calc_stats(data_file):
  data = np.loadtxt(data_file, delimiter=',')
  ave = np.mean(data)
  med = np.median(data)

  return round(ave,1), round(med,1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)
