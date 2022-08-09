from typing import List


def numFactoredBinaryTrees(arr: List[int]) -> int:
    MOD = 10 ** 9 + 7
    arr.sort()
    n = len(arr)
    dp = [1] * n
    idx_map = {item: i for i, item in enumerate(arr)}
    for i in range(n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and (arr[i] // arr[j]) in arr:
                q = idx_map[arr[i] // arr[j]]
                dp[i] += dp[j] * dp[q] % MOD
    return sum(dp) % MOD


print(numFactoredBinaryTrees([2, 4, 5, 10, 20]))
