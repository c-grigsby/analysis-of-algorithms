# Time Complexity: O(m*n), where m & n are the dimensions of the 2D array

def lcs_bottomup_helper(str1, str2, len_str1, len_str2):
   cache = [[0 for i in range(len_str2+1)] for i in range(len_str1+1)]
   
   for i in range(len_str1+1): 
      for j in range(len_str2+1): 
        
        if i == 0 or j == 0: cache[i][j] = 0
        
        elif str1[i-1] == str2[j-1]: cache[i][j] = cache[i-1][j-1] + 1
        
        else: cache[i][j]= max(cache[i-1][j] , cache[i][j-1])

   return cache[len_str1][len_str2]

def lcs_bottomup(str1, str2):
  if str1 == "" or str2 == "": return 0
  return lcs_bottomup_helper(str1, str2, len(str1) , len(str2))

if __name__ == '__main__':
  string1 = "abcdefg"
  string2 = "bdf"
  print("Length of longest common subsequence:", lcs_bottomup(string1, string2))