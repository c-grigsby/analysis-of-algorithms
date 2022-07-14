# Time: O(mn) Space: O(n) 
def lcs(str1, str2):
  if str1 == "" or str2 == "": return 0
  lcs_solution = []
  i = 0

  while i < len(str1):
    for j in range(len(str2)):
      if str1[i] == str2[j]: 
        lcs_solution.append(str1[i])
        
        str1 = str1[slice(i+1, len(str1))]
        str2 = str2[slice(j+1, len(str2))]
        
        if len(str1) == 0 or len(str2) == 0: return lcs_solution
        i = 0
        break
      
      if j == len(str2)-1: i += 1
      
  return lcs_solution

if __name__ == "__main__":
  str1 = "AXYBC"
  str2 = "ABCXY"
  result = lcs(str1, str2)
  print("Longest common subsequence: %s Length: %d" %(result, len(result)))