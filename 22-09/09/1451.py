class Solution:
    def arrangeWords(self, text: str) -> str:
        t = text.split(" ")
        t.sort(key=lambda x: len(x))
        res = " ".join(t).lower()
        res = res[0].upper() + res[1:]
        return res
