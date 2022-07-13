# Bottom-up approach
# Time Complexity: O(nW) where n is the number of items & W is the max_weight
# Space Complexity: O(W) 
def knapsack_unbounded(max_weight, item_weights, item_values):
  if max_weight == 0: return 0
  dp = [0 for i in range(max_weight + 1)]
  n = len(item_weights)
  
  for i in range(1, max_weight+1):
    current_weight = i
    for j in range(n):
      if item_weights[j] <= current_weight:
        dp[current_weight] = max(dp[current_weight], dp[current_weight - item_weights[j]] + item_values[j])
  
  return dp[max_weight]
  
# Driver
max_weight = 6
item_weights = [1, 2, 3, 4]
item_values = [10, 20, 5, 15]
print(knapsack_unbounded(max_weight, item_weights, item_values))