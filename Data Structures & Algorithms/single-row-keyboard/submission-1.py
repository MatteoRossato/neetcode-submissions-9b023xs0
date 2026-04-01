class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        myDict = {}
        i = 0

        for c in keyboard:
            myDict[c] = i
            i += 1

        j = 0 
        counter = 0
        for c in word: 
            counter += abs(myDict[c]-j)
            j = myDict[c]

        return counter 