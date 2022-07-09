# Time Complexity: O(2^n) 

def lcs_BF_helper(str1, str2, m, n):

  if m < 0 or n < 0: return 0

  elif str1[m] == str2[n]: return 1 + lcs_BF_helper(str1, str2, m-1, n-1)

  else: return max(lcs_BF_helper(str1, str2, m-1, n), lcs_BF_helper(str1, str2, m, n-1))

def lcs_BF(str1, str2):
  return lcs_BF_helper(str1, str2, len(str1)-1, len(str2)-1)

if __name__ == '__main__':
  string1 = "abcdefg"
  string2 = "bdf"
  print("Length of longest common subsequence:", lcs_BF(string1, string2))

