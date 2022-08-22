from typing import List, Tuple


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> Tuple[int, List[int]]:
        # Use dp[i][j] to represent the farthest distance it can get at station i and with j stops
        n = len(stations)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = startFuel

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j]
                if dp[i - 1][j - 1] >= stations[i - 1][0]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1])
        print(dp)

        for j in range(i + 1):
            if dp[i][j] >= target:
                return j

        return -1

        # Trace back the path of the solution from dp[n][k]
        # path = []
        # i = n
        # j = k
        # while i > 0:
        #     if dp[i][j] == dp[i - 1][j]:
        #         i -= 1
        #     else:
        #         path.append(i)
        #         i -= 1
        #         j -= 1
        # return k, path[::-1]


if __name__ == "__main__":
    # target = 100, startFuel = 10, stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    # In order to arrive at xn, either refill at the previous station or not
    # Use dp[i][j] to represent the farthest distance it can get at station i and with j stops
    # answer find j such that dp[n][j] >= target
    # transition function dp[i][j] = max(dp[i-1][j-1] + fuel(i), dp[i-1][j])
    # order i from 0 to n; j from 0 to n

    target = 100
    startFuel = 10
    stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
    print(Solution().minRefuelStops(target, startFuel, stations))
