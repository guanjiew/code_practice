def find132pattern(nums: List[int]) -> bool:
    i, j = 0, len(nums) - 1
    while i < j - 1:
        if nums[i] >= nums[j]:

