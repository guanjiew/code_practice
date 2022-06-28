def minDeletions(s: str) -> int:
    char_freq = [0] * 26
    for c in s:
        char_freq[ord(c) - ord("a")] += 1
    seen_freq = set()
    deletion = 0
    for freq in char_freq:
        while freq != 0 and freq in seen_freq:
            deletion += 1
            freq -= 1
        seen_freq.add(freq)
    return deletion
