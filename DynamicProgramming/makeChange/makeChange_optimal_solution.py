def makechange(coins, amount):
    # setting array elements to some large value that is not possible answer
    min_count_table = [amount+1]*(amount+1) 
    coin_used = [ 0 for _ in range(amount+1)]
    # setting the base case
    min_count_table[0] = 0 
    # iterate through all possible amount values from base case
    for amnt in range(1, amount+1): 
        #find the number of coins needed for each coin denomination 
        for coin_itr in range(0, len(coins)): 
            coin_val = coins[coin_itr]
            # if denomination value is less than amount then we can use the coin
            if(coin_val <= amount): 
                #if we found new best solution
                if(min_count_table[amnt-coin_val]+1 < min_count_table[amnt]): 
                    min_count_table[amnt] = min_count_table[amnt-coin_val]+1
                    coin_used[amnt] = coin_val
    # we have a valid count of coins if min_count_table[amount] is valid
    if min_count_table[amount] > amount: result = -1
    else: result = min_count_table[amount]

    solution = []
    # get the coins to be used
    while amount>0:
        solution.append(coin_used[amount])
        amount = amount-coin_used[amount]

    return result, solution

amount = 8
coins = [1, 3, 5]
result = makechange(coins, amount)
print("\nMinimum coins that can be used to disperse %d cents:" %(amount), result[0])
print("Coins used:", result[1])