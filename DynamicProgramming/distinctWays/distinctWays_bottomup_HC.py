# If the values of the blocks can be hard-coded (HC), this algorithm can be made slightly more efficient than the dynamic bottom-down approach. Base values will need to be computed then initilaized for i, i+1, i+2, these are then used to calculate the value of i+3 to n. 

# Time Complexity: O(n) Space Complexity: O(n)
def distinctWays_bottomup(num):
  block_1 = 1
  block_2 = 2
  
  if num < 0: return 0
  cache = [0 for i in range(num+1)]

  # base cases for cache
  cache[0] = 0
  if num >= 1: cache[1] = 1
  if num >= 2: cache[2] = 2
  
  for i in range(3, num+1):
    cache[i] = cache[i - block_1] + cache[i - block_2]
    
  return cache[num]
  
if __name__ == "__main__":
  num = 0
  print("The number of distinct ways the blocks can form the number is:", distinctWays_bottomup(num))  