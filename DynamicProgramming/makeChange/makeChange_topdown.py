import sys


def makechange_topdown( coins, amount):
    if amount == 0:
        return 0
    return makechange_topdown_helper(coins, amount, [0] * (amount + 1))


def makechange_topdown_helper( coins, amount, countmemo):
    if (amount < 0): return -1
    if (amount == 0): return 0
    if (countmemo[amount] != 0): return countmemo[amount]
    # set to some maximum value
    inf = sys.maxsize
    minimum_coins = sys.maxsize  
    
    for coin in coins:
        temp_coincount = makechange_topdown_helper(coins, amount - coin, countmemo)

        if (temp_coincount >= 0 and temp_coincount < minimum_coins):
            minimum_coins = 1 + temp_coincount
    # if we found a new minimum use it
    countmemo[amount] = -1 if (minimum_coins == inf) else minimum_coins 

    return countmemo[amount]


print(makechange_topdown([5,3,1], 9))