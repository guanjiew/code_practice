# Bowling
# • Given n pins labeled 0, 1, . . . , n − 1
# • Pin i has value vi
# • Ball of size similar to pin can hit either
# – 1 pin i, in which case we get vi points
# – 2 adjacent pins i and i + 1, in which case we get vi · vi+1 points
# • Once a pin is hit, it can’t be hit again (removed)
# • Problem: Throw zero or more balls to maximize total points
# • Example: [ −1, 1 , 1 , 1 , 9, 9 , 3 , −3, −5 , 2, 2 ]

# Sub-problem: BOWLING[:i] the maximum value to can get consider pin from 0 to i
# Relation: BOWLING[i] = max(BOWLING[i-1], BOWLING[i-1] + pins[i], BOWLING[i-2] + pins[i] * pins[i-1])
# Initialization: BOWLING[0] = max(pins[0], 0)
# Order: i from 1 to n
# Time: O(n)
# Space: O(n)
def bowling(pins):
    BOWLING = [0] * len(pins)
    BOWLING[0] = max(pins[0], 0)
    BOWLING[1] = max(BOWLING[0], BOWLING[0] + pins[1], pins[0] * pins[1])
    for i in range(2, len(pins)):
        BOWLING[i] = max(BOWLING[i - 1], BOWLING[i - 1] + pins[i], BOWLING[i - 2] + pins[i] * pins[i - 1])
    print(BOWLING)
    return BOWLING[-1]


pin1 = [-1, 1, 1, 1, 9, 9, 3, -3, -5, 2, 2]
print(bowling(pin1))


def bowling_memo(pins):
    # Use recursive memoization to solve the problem
    # Time: O(n)
    # Space: O(n)
    memo = {}

    def bowling_rec(i):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[i] = max(pins[0], 0)
        elif i == 1:
            memo[i] = max(bowling_rec(i - 1), bowling_rec(i - 1) + pins[1], pins[0] * pins[1])
        else:
            memo[i] = max(bowling_rec(i - 1), bowling_rec(i - 1) + pins[i], bowling_rec(i - 2) + pins[i] * pins[i - 1])
        return memo[i]

    return bowling_rec(len(pins) - 1)


print(bowling_memo(pin1))
