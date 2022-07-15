from copy import deepcopy

def powerset_helper(pointer, choices_made,input, result):
    if (pointer < 0):
        result.append(deepcopy(choices_made)) # make a deep copy since we are working with objects
        return 

    choices_made.append(input[pointer])
    powerset_helper(pointer-1, choices_made, input, result)
    #backtracking
    choices_made.pop() #remove last element added to choices_made
    powerset_helper(pointer - 1, choices_made, input, result)


def powerset(input):
    result = []
    powerset_helper(len(input)-1, [], input, result)
    print("Result:", result)

# Driver
input = [1, 2, 3]
powerset(input)
