import collections


def isPossible(nums):
    freq = collections.Counter(nums)
    next_num = collections.Counter()
    for num in nums:
        if freq[num] == 0:
            continue
        if next_num[num] > 0:
            next_num[num] -= 1
            next_num[num + 1] += 1
        elif freq[num + 1] > 0 and freq[num + 2] > 0:
            freq[num + 1] -= 1
            freq[num + 2] -= 1
            next_num[num + 3] += 1
        else:
            return False
        freq[num] -= 1
    return True


if __name__ == '__main__':
    print(isPossible([1, 2, 3, 4, 5]))
