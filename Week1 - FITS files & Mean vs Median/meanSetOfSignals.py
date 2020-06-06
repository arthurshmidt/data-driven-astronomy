# Write your mean_datasets function here
import numpy as np

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


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
