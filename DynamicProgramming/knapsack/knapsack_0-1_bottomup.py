# Time Complexity: O(nW) where n is the number of items & W is the max_weight
# Space Complexity: O(nW)
def knapsack_01(max_weight, item_weights, item_values):
  if max_weight == 0: return 0
  n = len(item_weights)
  dp = [[0 for i in range(n+1)] for i in range(max_weight+1)]
  
  for x in range(1, max_weight+1):
    for i in range(1, n+1):
      vi = item_values[i-1]
      wi = item_weights[i-1]
      if x >= wi:
        dp[x][i] = max(vi + dp[x - wi][i-1], dp[x][i-1])
  
  return dp[max_weight][n]

# Driver
item_weights = [4, 9, 3, 5, 7]
item_values = [10, 25, 13, 20, 8]
max_weight = 10
print(knapsack_01(max_weight, item_weights, item_values))