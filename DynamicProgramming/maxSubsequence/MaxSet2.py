def max_independent_set(nums):
  memo = {-1: 0, -2: 0}
  n = len(nums)
  subset = []
  for i in range(n):
      memo[i] = max(memo[i - 1], nums[i]+memo[i - 2], nums[i], memo[i-2])

  if memo[i] == 0: return [0]
  
  k = n - 1
  values = list(memo.values())
  while k >= 0:
      if values[k] != values[k-1]:
          subset.append(nums[k])
          k -= 1
      k -= 1
      
  return list(reversed(subset))

if __name__ == "__main__":
  numbers1 = [7, 2, 5, 8, 6]
  numbers2 = [-1, -1, 0]
  numbers3 = [-1, -1, -10, -34]
  result = max_independent_set(numbers2)
  print("Max subsequence of non-consecutive numbers:", result)