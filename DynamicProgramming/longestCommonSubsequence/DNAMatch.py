def dna_match_topdown_helper(str1, str2, len_str1, len_str2, cached):
  cache = cached
  if len_str1 < 0 or len_str2 < 0: return 0 
  
  if len_str1 == 0 or len_str2 == 0: return cache[len_str1][len_str2]
  
  if cache[len_str1][len_str2] != 0: return cache[len_str1][len_str2]
  
  elif str1[len_str1 -1] == str2[len_str2 -1]: 
    cache[len_str1][len_str2] = 1 + dna_match_topdown_helper(str1, str2, len_str1 -1, len_str2 -1, cache)
    return cache[len_str1][len_str2]
  
  else: 
    cache[len_str1][len_str2] = max(dna_match_topdown_helper(str1, str2, len_str1 -1, len_str2, cache), dna_match_topdown_helper(str1, str2, len_str1, len_str2 -1, cache))
    return cache[len_str1][len_str2]

def dna_match_topdown(str1, str2):
  if str1 == "" or str2 == "": return 0
  cache = [[0 for i in range(len(str2)+1)] for i in range((len(str1)+1))]
  return dna_match_topdown_helper(str1, str2, len(str1), len(str2), cache)


def dna_match_bottomup_helper(str1, str2, len_str1, len_str2):
   cache = [[0 for i in range(len_str2+1)] for i in range(len_str1+1)]
   
   for i in range(len_str1+1): 
      for j in range(len_str2+1): 
        
        if i == 0 or j == 0: cache[i][j] = 0
        
        elif str1[i-1] == str2[j-1]: cache[i][j] = cache[i-1][j-1] + 1
        
        else: cache[i][j]= max(cache[i-1][j] , cache[i][j-1])

   return cache[len_str1][len_str2]

def dna_match_bottomup(str1, str2):
  if str1 == "" or str2 == "": return 0
  return dna_match_bottomup_helper(str1, str2, len(str1) , len(str2))

if __name__ == '__main__':
  string1 = "ATAGTTCCGTCAAA"
  string2 = "GTGTTCCCGTCAAA"
  print("Length of longest common subsequence using top-down approach:", dna_match_topdown(string1, string2))
  print("Length of longest common subsequence using bottom-up approach:", dna_match_bottomup(string1, string2))