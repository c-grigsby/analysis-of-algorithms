from copy import deepcopy

def amount_helper(numArr, start, result, remainder, combination):
  # base case
  if remainder == 0: # combo satisfies
    if sorted(combination) not in result: result.append(deepcopy(combination))
    return
  if remainder < 0: return # combo sum exceeds desired target
  
  # form the the recurssion tree
  for i in range(start, len(numArr)):
      combination.append(numArr[i])
      # push i forward +1 
      amount_helper(numArr, i+1, result, remainder - numArr[i], combination)
      #backtrack 
      combination.pop()

def amount(A, S):
  numArr = A
  targetSum = S
  start = 0
  result = []
  combination = []
  amount_helper(numArr, start, result, targetSum, combination)
  return result

if __name__ == "__main__":
  A = [11,1,3,2,6,1,5]
  S = 8
  result = amount(A, S)
  print("The possible unique combinations from the given amount is:", result)