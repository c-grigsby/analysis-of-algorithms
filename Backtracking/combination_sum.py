from copy import deepcopy

#Time: O(n^k) where n is the length of array to interrogate and k is the target sum
def combination_sum_helper(nums, start, result, remainder, combination):
    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

# Driver
arr = [11,1,3,2,6,1,5]
sum = 8
combination_sum(arr, sum)