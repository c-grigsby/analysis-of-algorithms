def makechange_bottomup(coins, amount):
    # setting array elements to some large value that is not possible answer
    min_count_table = [amount+1]*(amount+1) 
    # setting the base case
    min_count_table[0] = 0 
    # iterate through all possible amount values from base case
    for i in range(1, amount+1):
        #find the number of coins needed for each coin denomination 
        for j in range(0, len(coins)): 
            coin_val = coins[j]
            # if denomination value is less than amount then we can use the coin
            if(coin_val <= amount and (i-coin_val)>=0):
                # replace min_count_table[i] with minumum value of coins possible
                min_count_table[i] = min(min_count_table[i] , min_count_table[i-coin_val]+1)
    # we have a valid count of coins if min_count_table[amount] is valid
    if min_count_table[amount] > amount: result = -1
    else: result = min_count_table[amount]
    
    return  result

print(makechange_bottomup([1,3,5], 8))