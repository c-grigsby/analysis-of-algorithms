# Time: O(n) Space: O(n^2)
def max_independent_set(numArr):
  arr_length = len(numArr)
  if numArr[0] < 0: return []
  elif arr_length == 0 or arr_length == 1: return numArr
  cache = [0 for i in range(arr_length)]
  solution = []
  # base cases for cache
  if arr_length >= 1: cache[0] = numArr[0]
  if arr_length >= 2: cache[1] = max(numArr[0], numArr[1])
  # obtain the max total from the cache
  for i in range(2, arr_length):
    cache[i] = max(numArr[i] + cache[i-2], cache[i-1], numArr[i], cache[i-2])
  maxTotal = cache[arr_length-1]
  # if max is less than or equal to zero 
  if maxTotal < 0: return []
  elif maxTotal == 0: return [0]
  # use the recurrence equation and maxTotal to iterate back for the values
  currentTotal = maxTotal
  i = arr_length-1
  while i >= 0 and currentTotal > 0: 
    #case 1
    if numArr[i] + cache[i-2] == currentTotal:
      solution.append(numArr[i])
      currentTotal -= numArr[i]
      i -= 2
    #case 2
    elif numArr[i-1] + cache[i-3] == currentTotal:
      solution.append(numArr[i-1])
      currentTotal -= numArr[i-1]
      i -= 3
    # case 3
    elif numArr[i] == currentTotal:
      solution.append(numArr[i])
      currentTotal -= numArr[i]
      i -= 1
    # case 4
    elif numArr[i-1] == currentTotal:
      solution.append(numArr[i-1])
      currentTotal -= numArr[i-1]
      i -= 1
    # return error
    else: return solution.append("Error")
  
  # reverse the solution array and return
  solution.reverse()
  return solution

if __name__ == "__main__":
  numbers1 = [7, 2, 5, 8, 6]
  numbers2 = [-1]
  numbers3 = [-1, -1, -10, -34]
  result = max_independent_set(numbers2)
  print("Max subsequence of non-consecutive numbers:", result)