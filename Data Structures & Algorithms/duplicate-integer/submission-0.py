class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = Counter(nums)
        for val in myDict.values():
            if val > 1:
                return True
        
        return False