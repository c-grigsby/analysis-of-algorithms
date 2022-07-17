# Time: O(n) Space: O(n^2)
def max_independent_set(numArr):
    cache = {-1: 0, -2: 0}
    n = len(numArr)
    subset = []

    for i in range(n):
        cache[i] = max(cache[i - 1], cache[i - 2] + numArr[i])

    i = n - 1
    while i >= 0:
        if cache[i] != cache[i-1]:
            subset.append(numArr[i])
            i -= 1
        i -= 1

    if subset == [] and 0 in numArr: subset.append(0)

    return list(reversed(subset))

if __name__ == "__main__":
  numbers1 = [7, 2, 5, 8, 6]
  numbers2 = [-1, -1, 0]
  numbers3 = [-1, -1, -10, -34]
  result = max_independent_set(numbers1)
  print("Max subsequence of non-consecutive numbers:", result)