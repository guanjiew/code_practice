def mySqrt(x: int) -> int:
    l = 0
    r = x
    if x >= 4:
        r = x // 2
    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid == x or mid * mid < x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


mySqrt(1)
