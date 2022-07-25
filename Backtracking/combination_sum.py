from copy import deepcopy

#Time: O(n^k) where n is the length of array & k is the target sum
def combination_sum_helper(nums, start, result, remainder, combination):
    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    # sum exceeded the target
    elif( remainder < 0): return 
    
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

# driver
arr = [2, 3, 6, 7]
sum = 7
combination_sum(arr, sum)