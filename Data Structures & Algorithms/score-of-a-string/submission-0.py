class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0
        for i in range(len(s)-1):
            first = ord(s[i])
            second = ord(s[i+1])
            tot += abs(second-first)
        
        return tot