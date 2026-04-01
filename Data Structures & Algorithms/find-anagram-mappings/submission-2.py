class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        valueToPos = {}
        stack = []

        for i in range(len(nums2)):
            valueToPos[nums2[i]] = i
        
        for i in nums1:
            stack.append(valueToPos[i])
        
        return stack
