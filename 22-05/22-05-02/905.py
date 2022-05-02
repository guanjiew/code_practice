# https://leetcode.com/problems/sort-array-by-parity/
# S1: Traverse through the array and rebuild the new array TC:O(N) SC:O(N)
def sortArrayByParity(nums: List[int]) -> List[int]:
    ans = []
    for num in nums:
        if num % 2 == 0:
            ans.insert(0, num)
        else:
            ans.append(num)
    return ans


# S2: Use a custom compartor when sorting TC:O(Nlog(N)) SC:O(N)
def sortArrayByParitySort(nums):
    nums.sort(key=lambda x: x % 2)
    return nums


# S3: Use an in-place sort on the array, say we have indexed i, j
# then array[:i) are element 0, array(j:] are element 1
# TC:O(N) SC:O(1)
def sortArrayInplace(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i + 1] % 2 == 0:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
    return nums
