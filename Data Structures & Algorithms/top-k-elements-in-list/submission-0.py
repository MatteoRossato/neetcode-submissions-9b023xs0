class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        output = []
        keys_sorted = sorted(d, key=d.get, reverse=True)

        output = keys_sorted[:k]
        return output
