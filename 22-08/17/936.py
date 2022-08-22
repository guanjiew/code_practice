from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        Example1, stamp="abc", target="abcba", covert s "?????" into target via stamp
        s = "abcba" => "???ba"
        "???ba" => "?????"
        Go through the sequence s and replace the first detected matched sequence and replace with ?,
        log the index into a list. If there is no matched sequence, return empty list
        """
        res = []
        while target != "?" * len(target):
            idx = self.match(stamp, target, set(res))
            if idx != -1:
                target = target[:idx] + '?' * len(stamp) + target[idx + len(stamp):]
                res.insert(0, idx)
            else:
                return []
        return res

    def match(self, stamp, target, seen):
        """
        Find the first occurrence of the stamp in target and replace the sequence with ?
        If stamp cannot be found, return -1; otherwise return the index
        """
        for i in range(len(target) - len(stamp) + 1):
            if i in seen:
                continue
            if self.isEqual(stamp, target[i:i + len(stamp)]):
                return i
        return -1

    def isEqual(self, stamp, target):
        """
        Check if stamp is equal to target
        """
        assert len(stamp) == len(target)
        for i in range(len(target)):
            if target[i] != stamp[i] and target[i] != '?':
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    stamp = "xkaa"
    target = "xkaaaaxkaaaxxkaaaaaxkxkaxkxkaaaxxxkaakaxkaakaaaxkaaaakaxkaakxkaaaaxkxkxkaaaxxkxkaaxkaxkaaaakxkaaaxkxkaaaakxkaaxkaaaxkaakxkaaaxkaaakaakxxkaxkaakxxkaakaaxkaxkaaakaxkxkaaxkaxkaaaxkaxkaxkaakaaxkaakaakxkaaaxxkaaxkaaaaaxkaaxxkaakaakaaaakxkaaaaaxkaaaxxkaaxkxkaaxkaaakaaxkaxkaaxkaxkaakaxkaaxkaakxkaaaxkxkaaxkaaaxkaaaxkaaxkaaxkaxkaakaaaaaaaxkaaaxkaxkxkaaxkxkaaxkaaxkxxkaaaxkaaaxkaaaxkaaxxkxkaaxkxkaakaakxkaaxkaaaxkaaxkaaaakaxkaaaxkaakaxkaaaxkaaxkaxkaaaxxkaaaakaxxkaakxkaaaaaxxkaaxxkaaaxkaaxxkaaakxxkaaaaaxxkxkaxkaakxxkaaxkaaaakxxkaaxkaaaaaaxkxkaaxxxkaaxxkaaxkaxkaakaxkaakaaaakxkaakaxkxkaaaaxxxkaakaaxkaaxkaaxkaaxxkaakaaaxkaxkaaxkxkaaaxkaakaakxkxkaaaaakaxkaxxxxkaaxkaaxkaaaxkaaaxkaaakxkxkaaaxkaaxkxkaxkaakaxkaaxkxkaaaxxkaaaaaaxkaaaaxkxkaaaaaxkaaaaxxkaaxkaaaaaxkaaxxkaaxkxkaaaaxkaakaakaaxkaaxkaaaxkaaaaaxxxkaaxkaaaaxkaaaxkaaxkaaxkaaxkaaxkaaaaxkaakaxkaaaxkaaaxxkaaakxkaxkaaaxxkaaaaxkxkaxkaaaaakxxkxkaaxkaxkaaakaxkxkaaxkxxkxkaaaaxxxxkaakaakaakaaxxxxkaaxkaakaaaaakxxxkaaxxxkxkaaaaxxkaaaxxkaaaaaxkxkaxkaaxkaaaxxkaaa "
    print(s.movesToStamp(stamp, target))
