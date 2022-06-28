from collections import defaultdict


def minDeletions(s: str) -> int:
    char_freq = defaultdict(lambda: 0)
    for c in s:
        char_freq[c] += 1
    freq_occ = defaultdict(lambda: 0)
    for c in char_freq:
        freq_occ[char_freq[c]] += 1
    deletion = 0
    freq = sorted(freq_occ.keys(), reverse=True)
    for i, f in enumerate(freq):
        f_occ = freq_occ[f]
        if f_occ == 1:
            continue
        else:
            nxt_f = 0
            if i < len(freq) - 1:
                nxt_f = freq[i + 1]
            gap = f - nxt_f - 1
            drop_bet_nxt_f = min(f_occ - 1, gap)
            deletion += drop_bet_nxt_f * (drop_bet_nxt_f + 1) // 2
            drop_to_nxt_f = max(0, f_occ - gap - 1)
            deletion += (f - nxt_f) * drop_to_nxt_f
            freq_occ[nxt_f] += drop_to_nxt_f
    return deletion
