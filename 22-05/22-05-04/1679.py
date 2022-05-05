# https://leetcode.com/problems/max-number-of-k-sum-pairs/
def maxOperations1(nums: List[int], k: int) -> int:
    num_map = {}
    for num in nums:
        if num in num_map:
            num_map[num] += 1
        else:
            num_map[num] = 1
    ans = 0
    for num in nums:
        other = k - num
        if num in num_map and other in num_map:
            if num == other:
                if num_map[num] < 2:
                    continue
                else:
                    num_map[num] -= 2
                    ans += 1
                    if num_map[num] == 0:
                        del num_map[num]
            else:
                num_map[num] -= 1
                num_map[other] -= 1
                ans += 1
                if num_map[num] == 0:
                    del num_map[num]

                if num_map[other] == 0:
                    del num_map[other]
    return ans


def maxOperations_improve(nums: List[int], k: int) -> int:
    num_map = {}
    for num in nums:
        if num in num_map:
            num_map[num] += 1
        else:
            num_map[num] = 1
    ans = 0
    for num in nums:
        other = k - num
        if num in num_map and other in num_map:
            if num == other:
                ans += num_map[num] // 2
                del num_map[num]
            else:
                ans += min(num_map[num], num_map[other])
                del num_map[num]
                del num_map[other]
    return ans


def maxOperations2(nums: List[int], k: int) -> int:
    nums.sort()
    i, j = 0, len(nums) - 1
    ans = 0
    while i < j:
        s, e = nums[i], nums[j]
        if e > k - s:
            j -= 1
        elif s < k - e:
            i += 1
        elif e + s == k:
            ans += 1
            i += 1
            j -= 1
    return ans
