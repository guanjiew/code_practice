# https://leetcode.com/problems/count-vowels-permutation/
def countVowelPermutation(n: int) -> int:
    vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    for i in range(2, n + 1):
        new_vowels = {'a': vowels['e'] + vowels['i'] + vowels['u'], 'e': vowels['a'] + vowels['i'],
                      'i': vowels['e'] + vowels['o'], 'o': vowels['i'], 'u': vowels['o'] + vowels['i']}
        vowels = new_vowels
    return sum(vowels.values()) % (10 ** 9 + 7)
