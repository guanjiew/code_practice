def maximumUniqueSubarray(nums):
    seen = set()
    curr_sum, max_sum = 0, 0
    l = 0
    for num in nums:
        while num in seen:
            curr_sum -= nums[l]
            l += 1
        curr_sum += num
        seen.add(num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

maximumUniqueSubarray([4, 2, 4, 5, 6])
