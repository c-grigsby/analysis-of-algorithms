# Time Complexity: O(n) Space Complexity: O(n)
def distinctWays_topdown_helper(num, cached, blocks): 
  cache = cached
  if num < 0: return 0
  if num == 0: return 1
  if cache[num] != 0: return cache[num]
  
  cache[num] = distinctWays_topdown_helper(num - blocks[0], cache, blocks) + distinctWays_topdown_helper(num - blocks[1], cache, blocks)
  
  return cache[num]

def distinctWays_topdown(num, blocks = [1,2]):
  if num <= 0: return 0
  if (blocks[0] == 0 or blocks[1] == 0) or (blocks[0] == blocks [1]) or len(blocks) != 2: 
    return "Error. Blocks must be two distinct integers greater than zero"
 
  cache = [0 for i in range(num+1)]
  return distinctWays_topdown_helper(num, cache, blocks)

if __name__ == '__main__':     
  blocks = [1, 2]
  num = 4
  print("The number of distinct ways the blocks can form the number is:", distinctWays_topdown(num, blocks))