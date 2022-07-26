# Longest Common Subsequence
# Given two sequences, find the longest subsequence common to both of them.
# Problems for multiple inputs: multiply subproblems spaces
# subproblem : L[i,j] = LCS(A[i:], B[j:])
# L[i,j] = 1 + L[i+1,j+1] if A[i] == B[j]
# L[i,j] = max{L[i,j+1], L[i+1,j]} if A[i] != B[j]
