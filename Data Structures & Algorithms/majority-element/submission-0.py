class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}

        for n in nums: 
            if n in myDict:
                myDict[n] += 1
            else:
                myDict[n] = 1
        
        return max(myDict, key=myDict.get)