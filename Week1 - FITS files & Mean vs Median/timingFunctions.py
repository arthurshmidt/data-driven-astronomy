import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  average_times = []
  for n in range(ntrials):
    # the time to generate the random array should not be included
    data = np.random.rand(size)
    # modify this function to time func with ntrials times using a new random array each time
    start = time.perf_counter()
    res = func(data)
    seconds = time.perf_counter() - start
    average_times.append(seconds)

  # return the average run time
  return sum(average_times)/len(average_times)

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))
