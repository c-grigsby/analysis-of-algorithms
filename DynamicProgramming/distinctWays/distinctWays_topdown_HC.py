# Time Complexity: O(n) Space Complexity: O(n)
def distinctWays_topdown_helper(num, cached): 
  cache = cached
  block_1 = 1
  block_2 = 2
  # base cases
  if num < 0: return 0
  if num == 0: return 1
  # check if the subproblem was previously computed
  if cache[num] != 0: return cache[num]    
  
  cache[num] = distinctWays_topdown_helper(num - block_1, cache) + distinctWays_topdown_helper(num - block_2, cache)
  return cache[num]

def distinctWays_topdown(num):
  if num <= 0: return 0 
  # a list for memoization with a default value of 0 for all elements
  cache = [0 for i in range(num+1)]  
  return distinctWays_topdown_helper(num, cache)

if __name__ == "__main__":
  num = 5
  print("The number of distinct ways the blocks can form the number is:", distinctWays_topdown(num))  
