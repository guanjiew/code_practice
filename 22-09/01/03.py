def solution(N, K):
    # write your code in Python 3.6
    return pour(N, K)


def pour(n, k):
    if n <= 0:
        return -1
    if k <= n:
        return 1
    else:
        sub = pour(n - 1, k - n)
        if sub == -1:
            return -1
        else:
            return sub + 1


if __name__ == "__main__":
    print(solution(8, 10))

