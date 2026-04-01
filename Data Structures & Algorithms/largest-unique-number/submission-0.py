class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        myDict = Counter(nums)
        maxN = -1

        for i in myDict:
            if myDict[i] == 1:
                maxN = max(maxN, i)
            
        return maxN