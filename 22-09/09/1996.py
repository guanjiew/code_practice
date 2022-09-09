from typing import List


class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        # Sort by attack in descending order, if attack is equal, sort by defense in ascending order
        # If the defense of the current character is less than max defense we have seen so far,
        # then the character with the max defense is stronger than the current character;
        # For characters with the same attack, we store the defense in ascending order to
        # avoid comparison with the same attack.
        p.sort(key=lambda x: (-x[0], x[1]))
        max_defense = 0
        count = 0
        for attack, defense in p:
            if defense < max_defense:
                count += 1
            else:
                max_defense = defense
        return count


if __name__ == "__main__":
    properties = [[5, 5], [6, 3], [3, 6]]
    print(Solution().numberOfWeakCharacters(properties))

    properties = [[2, 2], [3, 3]]
    print(Solution().numberOfWeakCharacters(properties))

    properties = [[1, 1], [2, 1], [2, 2], [1, 2]]
    print(Solution().numberOfWeakCharacters(properties))
