# Bottom-up approach
# Time Complexity: O(nW) where n is the number of items & W is the max_weight
# Space Complexity: O(W) 
def knapsack_unbounded(max_weight, item_weights, item_values):
  if max_weight == 0: return 0
  dp = [0 for i in range(max_weight + 1)]
  bestItem = [0 for i in range(max_weight + 1)]
  n = len(item_weights)
  
  for i in range(1, max_weight+1):
    current_weight = i
    for j in range(n):
      if item_weights[j] <= current_weight:
        if dp[current_weight - item_weights[j]] + item_values[j] > dp[current_weight]:
          dp[current_weight] = dp[current_weight - item_weights[j]] + item_values[j]
          bestItem[current_weight] = item_weights[j]

  w = max_weight    
  solutionItems = []
  while w > 0:
    solutionItems.append(bestItem[w])
    w = w - bestItem[w]
    
  return dp[max_weight], solutionItems
  
# Driver
max_weight = 99
item_weights = [4, 9, 3, 5, 7]
item_values = [10, 25, 13, 20, 8]
result = knapsack_unbounded(max_weight, item_weights, item_values)
print("Max value to be earned for transporting the goods with a given weight restriction of %s lbs: $%s" %(max_weight, result[0]))
print("The item weights that are to be used are:", result[1])