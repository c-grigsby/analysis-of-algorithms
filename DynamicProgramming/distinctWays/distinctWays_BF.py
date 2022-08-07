# Time Complexity: O(2^n) Space Complexity: O(1)
def distinctWays_BF(num, blocks = [1,2]): 
  if num < 0: return 0
  elif num == 0: return 1
  
  return distinctWays_BF(num - blocks[0], blocks) + distinctWays_BF(num - blocks[1], blocks)

# Time Complexity: O(2^n) Space Complexity: O(1)
def distinctWays_BF2(num):  
  if num < 0: return 0
  elif num == 0: return 1
  
  return distinctWays_BF2(num - 1) + distinctWays_BF(num - 2)

if __name__ == '__main__':     
  blocks = [1,2]
  randomNumber = 4
  print("The number of distinct ways the blocks can form the number is:", distinctWays_BF(randomNumber, blocks))
  print("The number of distinct ways the blocks can form the number is:", distinctWays_BF2(randomNumber))