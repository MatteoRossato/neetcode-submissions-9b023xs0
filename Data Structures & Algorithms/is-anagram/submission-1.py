class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = Counter(s)
        tDict = Counter(t)

        if sDict == tDict:
            return True
        else:
            return False