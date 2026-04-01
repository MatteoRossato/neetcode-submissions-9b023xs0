class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        myDict = Counter(arr)
        counter = 0
        for i in myDict:
            if i+1 in arr:
                counter += myDict[i]
        
        return counter