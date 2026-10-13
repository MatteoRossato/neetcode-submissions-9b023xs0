class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = []
        count.append(nums[0])

        for i in range(1,len(nums)):
            for j in range(len(count)):
                if nums[i] + count[j] == target:
                    return [j, i]
            count.append(nums[i])