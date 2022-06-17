"""
Approach 1:
Cache the prefix sum and iterate through suffix sum to find match with target
Space: O(n)
Time: O(n)
"""


# Using enumerate:
# https://realpython.com/python-enumerate/
def minOperation1(nums, target):
    # Map between prefix sum to index
    prefix_map = {0: -1}
    prefix_sum = 0
    for i, x in enumerate(nums):
        prefix_sum += x
        prefix_map[prefix_sum] = i
    operations = float("inf")
    if target in prefix_map:
        operations = prefix_map[target] + 1
    suffix_sum = 0
    for j, x in enumerate(reversed(nums)):
        suffix_sum += x
        prefix_left = target - suffix_sum
        if prefix_left in prefix_map:
            index = prefix_map[prefix_left]
            if len(nums) - 1 - j > index:
                operations = min(operations, index + j + 2)
    if operations == float("inf"):
        return -1
    else:
        return operations
