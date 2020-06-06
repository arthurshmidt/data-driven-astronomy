# Write your list_stats function here.
def list_stats(values):
  if (len(values) % 2) == 0:

    # Median Calculation
    values.sort()
    mid = len(values)//2
    median = (values[mid - 1] + values[mid])/2

    # Mean Calculation
    mean = sum(values)/len(values)
    return median, mean

  else:

    # Median Calculation
    values.sort()
    mid = len(values)//2
    median = values[mid]

    # Mean Calculation
    mean = sum(values)/len(values)
    return median, mean



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
