# Time: O(2^n) Space: O(1)
# Returns the maximum value from a subsequence of non-consective numbers
def max_subsequence_BF(numArr, i):
  if i <= 0: return 0
  if i == 1: return numArr[i-1]
  
  return max(numArr[i-1] + max_subsequence_BF(numArr, i-2), numArr[i-2] + max_subsequence_BF(numArr, i-3), numArr[i-1], numArr[i-2])
    
if __name__ == "__main__":
  numbers = [7, 2, 5, 50, 6, 9]
  numbers1 = [7, 2, 5, 8, 6]
  numbers2 = [-1, -1, 0]
  numbers3 = [-1, -1, -10, -34]
  print("Max value from a subsequence of non-consecutive numbers:", max_subsequence_BF(numbers, len(numbers)))
