class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        myW = ''
        for i in range(l):
            myW += word1[i] + word2[i]
            print(myW)
        
        if len(word1) > len(word2):
            myW += word1[l::]
        if len(word2) > len(word1):
            myW += word2[l::]
        return myW