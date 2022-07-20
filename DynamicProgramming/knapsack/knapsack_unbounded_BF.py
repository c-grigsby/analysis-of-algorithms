def knapsack_BF(max_weight, item_weights, item_values): 
  if max_weight <= 0: return 0
  result = 0
  
  for i in range(len(item_weights)):
    if item_weights[i] <= max_weight: 
      result = max(result, knapsack_BF(max_weight - item_weights[i], item_weights, item_values) + item_values[i])
  
  return result

# Driver 
max_weight = 4
item_weights = [1, 2, 3, 4]
item_values = [10, 20, 5, 15]
print (knapsack_BF(max_weight, item_weights, item_values))


