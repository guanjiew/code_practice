# https://leetcode.com/problems/mirror-reflection/
import math


# KEY STEP:
# 1. find the smallest common multiple of p and q
# 2. if lcm is odd multiple of p, it will reflect to the south wall, then the answer is 0
# 3. if lcm is even multiple of p, it will reflect to the north wall.
#   To determine the answer, we need to find the number of times the wall will reflect.
#   a. if lcm is odd multiple of q, it will reflect to the east wall, then the answer is 2
#   b. if lcm is even multiple of q, it will reflect to the west wall, then the answer is 1.

def mirrorReflection(p: int, q: int) -> int:
    lcm = (p * q) // math.gcd(p, q)
    if (lcm / p) % 2 == 0:
        return 0
    if (lcm / q) % 2 == 0:
        return 2
    return 1


if __name__ == "__main__":
    print(mirrorReflection(2, 1))
    print(mirrorReflection(3, 1))
