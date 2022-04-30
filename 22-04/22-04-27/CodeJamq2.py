# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
# A great DP practice, key observation is that each customer has to end with min or max pressure product
# Run-time complexity is O(N), space complexity is O(N)
def main():
    cases = int(input())
    for i in range(cases):
        n = int(input().split(" ")[0])
        Cps = []
        [Cps.append(list(map(int, input().split(" ")))) for j in range(n)]
        push = min_push(Cps)
        print("Case #{}: {}".format(i + 1, push))


def min_push(CPs):
    n = len(CPs)
    # Define P[i][0] as the minimum buttons to push serving C1 to Ci and if P(i,m) is the maximum product for Ci
    # Define P[i][1] as the minimum buttons to push serving C1 to Ci and if P(i,m) is the minimum product for Ci
    P = [[0] * 2 for i in range(n + 1)]
    # Define Opt as the array that stores the min, max pressure pair for each customer
    Opt = [(min(CPs[i]), max(CPs[i])) for i in range(n)]
    Opt.insert(0, (0, 0))
    for i in range(1, n + 1):
        ranges = Opt[i][1] - Opt[i][0]
        incr_incr_array = P[i - 1][0] + abs(Opt[i][0] - Opt[i - 1][1]) + ranges
        incr_decr_array = P[i - 1][1] + abs(Opt[i][0] - Opt[i - 1][0]) + ranges
        P[i][0] = min(incr_incr_array, incr_decr_array)
        decr_incr_array = P[i - 1][0] + abs(Opt[i][1] - Opt[i - 1][1]) + ranges
        decr_decr_array = P[i - 1][1] + abs(Opt[i][1] - Opt[i - 1][0]) + ranges
        P[i][1] = min(decr_incr_array, decr_decr_array)
    return min(P[n][0], P[n][1])


if __name__ == '__main__':
    main()
