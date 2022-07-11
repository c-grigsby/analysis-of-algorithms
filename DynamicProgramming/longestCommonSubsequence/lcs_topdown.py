# Time Complexity: O(m*n), where m & n are the dimensions of the 2D array

def lcs_topdown_helper(str1, str2, len_str1, len_str2, cached):
  cache = cached
  
  if len_str1 < 0 or len_str2 < 0: return 0 
  
  if len_str1 == 0 or len_str2 == 0: return cache[len_str1][len_str2]
  
  if cache[len_str1][len_str2] != 0: return cache[len_str1][len_str2]
  
  elif str1[len_str1 -1] == str2[len_str2 -1]: 
    cache[len_str1][len_str2] = 1 + lcs_topdown_helper(str1, str2, len_str1 -1, len_str2 -1, cache)
    return cache[len_str1][len_str2]
  
  else: 
    cache[len_str1][len_str2] = max(lcs_topdown_helper(str1, str2, len_str1 -1, len_str2, cache), lcs_topdown_helper(str1, str2, len_str1, len_str2 -1, cache))
    return cache[len_str1][len_str2]

def lcs_topdown(str1, str2):
  cache = [[0 for i in range(len(str2)+1)] for i in range((len(str1)+1))]
  return lcs_topdown_helper(str1, str2, len(str1), len(str2), cache)

if __name__ == '__main__':
  string1 = "abcdefg"
  string2 = "bdf"
  print("Length of longest common subsequence:", lcs_topdown(string1, string2))