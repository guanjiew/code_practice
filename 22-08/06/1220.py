# https://leetcode.com/problems/count-vowels-permutation/
def countVowelPermutation(n: int) -> int:
    vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    mods = 10 ** 9 + 7
    for i in range(2, n + 1):
        new_vowels = {'a': vowels['e'] + vowels['i'] + vowels['u'], 'e': vowels['a'] + vowels['i'],
                      'i': vowels['e'] + vowels['o'], 'o': vowels['i'], 'u': vowels['o'] + vowels['i']}
        vowels = new_vowels
    return sum(vowels.values()) % (10 ** 9 + 7)


def countVowelPermutation2(n: int) -> int:
    a, e, i, o, u = 1, 1, 1, 1, 1
    mods = 10 ** 9 + 7
    for i in range(2, n + 1):
        a, e, i, o, u = (e + i + u) % mods, (a + i) % mods, (e + o) % mods, i % mods, (o + i) % mods
    return (a + e + i + o + u) % mods
