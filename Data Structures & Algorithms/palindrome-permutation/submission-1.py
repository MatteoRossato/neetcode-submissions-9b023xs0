class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        count = Counter(s)
        odds = sum(val % 2 for val in count.values())
        return odds <= 1