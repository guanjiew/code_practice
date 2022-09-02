def solution(S):
    count = 0
    R_NUM = 0
    L_NUM = 0
    for i in range(len(S)):
        if S[i] == "R":
            R_NUM += 1
        else:
            L_NUM += 1
        if R_NUM == L_NUM:
            count += 1
            R_NUM = 0
            L_NUM = 0
    return count


if __name__ == "__main__":
    S = "RLRLLLRLRL"
    print(solution(S))
    S = "R"
    print(solution(S))
    S = "LL"
    print(solution(S))
    S = "RLRLRLRLRL"
    print(solution(S))
