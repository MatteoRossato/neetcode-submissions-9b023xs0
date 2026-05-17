class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0
        maxi = 0

        myDict = defaultdict(int)
        for n in nums:
            myDict[n] = myDict[n] + 1

        for k in myDict:
            if myDict[k] > maxi:
                maxi = myDict[k]
                res = k
        
        return res
            