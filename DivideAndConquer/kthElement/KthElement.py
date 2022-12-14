# Pseudocode
#
# def kthElement(Arr1, Arr2, k)                        // k is kth position of the element to return
# declare i, j, current_pos, kth_position = k-1
#
#   while i < len(arr1) and j < len(Arr2)
#    if Arr1[i] < Arr2[j]                              // traverse as if sorted merge 
#      if current_pos == kth_position                  // check for kth_position  
#        return Arr1[i]
#      i++
#    else 
#      if current_pos == kth_position                  // check for kth_position 
#        return Arr2[j]
#      j++
#    current_pos++
#
#   while i < len(Arr1)                                // traverse any remaining elements of Arr1
#    if current_pos == kth_position                    // check for kth_position 
#      return Arr1[i]
#    i++
#    current_pos++
#
#   while j < len(Arr2)                               // traverse any remaining elements of Arr2
#    if current_pos == kth_position                   // check for kth_position 
#      return Arr2[j]
#    j++
#    current_pos++
#
#   return -1                                         // not found
#
# Note: Based on the description provided, the element in position 0 of the array would be the 1st element


def kthElement(Arr1, Arr2, k): 
  i = 0 
  j = 0 
  current_pos = 0 
  kth_position = k - 1 

  while (i < len(Arr1) and j < len(Arr2)):
    # traverse as if sorted merge and check for Kth
    if Arr1[i] < Arr2[j]:                               
      if current_pos == kth_position: return Arr1[i]
      i += 1
    else:
      if current_pos == kth_position: return Arr2[j]
      j += 1
    current_pos += 1

  # traverse any remaining elements and check for Kth
  while i < len(Arr1):                           
    if current_pos == kth_position: return Arr1[i]
    i += 1
    current_pos += 1

  while j < len(Arr2):                         
    if current_pos == kth_position: return Arr2[j]
    j += 1
    current_pos += 1

  return -1

if __name__ == '__main__':
  Arr1 = [1,2,3,5,6]
  Arr2 = [3,4,5,6,7]
  k = 5
  print(kthElement(Arr1, Arr2, k))