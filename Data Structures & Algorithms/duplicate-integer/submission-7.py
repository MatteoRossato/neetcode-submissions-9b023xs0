class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = Counter(nums)
        if len(nums)!= len(myDict):
            return True
        
        return False