class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        #creo dizionario

        for i, n in enumerate(nums):
            diff = target - n
#con enumerate trovo valore e indice e calcolo differenza
#se ce nel Map allora c'è corrispettivo e restituisco indici

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i #altrimenti lo aggiungo