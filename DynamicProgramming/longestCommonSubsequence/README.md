LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
Assume that an empty string is not a subsequence of any string.

Example:

Input: str1 = "abcdef", str2 = "apceg"

output:  3

Explanation: The longest common subsequence is "ace" and its length is 3.

Note: This problem has many real-world applications, for instance when Git needs to merge two files it needs this algorithm, in biometrics -it is used to detect similarities between two genetic codes, and many more.

Question 1. 

##### _Solving Problems with Dynamic Programming_
