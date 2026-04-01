class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = Counter(s)
        secondDict = Counter(t)

        if firstDict == secondDict:
            return True
        
        return False