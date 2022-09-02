def solution(N, K):
    ns = str(N)
    d = 0
    incr = 0
    new_num = ""
    while incr <= K and d < len(ns):
        cur = int(ns[d])
        update = min(9-cur, K-incr)
        cur += update
        new_num += str(cur)
        incr += update
        d += 1
    return int(new_num)

if __name__ == "__main__":
    print(solution(512, 10))
    print(solution(123456789, 20))
    print(solution(123456789, 30))
    print(solution(123456789, 40))
