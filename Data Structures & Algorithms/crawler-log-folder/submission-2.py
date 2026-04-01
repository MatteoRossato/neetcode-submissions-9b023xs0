class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0

        for l in logs:
            if l == "../":
                if count != 0:
                    count -= 1
            elif l == "./":
                count += 0
            else:
                count += 1
        
        return count