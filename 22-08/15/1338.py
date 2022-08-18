import collections


def minSetSize(arr):
    arr_counter = collections.Counter(arr)
    freq = sorted(list(arr_counter.values()), reverse=True)
    rm = 0
    n = len(arr)
    m = 0
    for i in range(len(freq)):
        m += 1
        rm += freq[i]
        if rm >= n / 2:
            break
    return m


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 5, 2]
    print(minSetSize(arr))
