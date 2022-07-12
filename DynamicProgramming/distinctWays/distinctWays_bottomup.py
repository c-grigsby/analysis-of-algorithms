# Time Complexity: O(n) Space Complexity: O(n)
def distinctWays_bottomup_helper(num, cached, blocks):
  cache = cached
  
  if num < 0: return 0
  if num == 0: return 1
  if cache[num] != 0: return cache[num]
  
  for i in range(1, num+1):
    cache[i] = distinctWays_bottomup_helper(i - blocks[0], cache, blocks) + distinctWays_bottomup_helper(i - blocks[1], cache, blocks)
  
  return cache[num]
    
def distinctWays_bottomup(num, blocks = [1,2]):
  if num <= 0: return 0
  if (blocks[0] == 0 or blocks[1] == 0) or (blocks[0] == blocks [1]) or len(blocks) != 2: 
    return "Error. Blocks must be two distinct integers greater than zero"

  cache = [0 for i in range(num + 1)]
  return distinctWays_bottomup_helper(num, cache, blocks)
  
if __name__ == "__main__":
  blocks = [1, 2]
  num = 5
  print("The number of distinct ways the blocks can form the number is:", distinctWays_bottomup(num, blocks))  