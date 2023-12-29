#Given a non-empty array of integers nums,
#every element appears twice except for one.
# Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        
        pairs = set()
        
        for i in range(len(nums)):
            if nums[i] not in pairs:
                pairs.add(nums[i])
            else:
                pairs.remove(nums[i])
        
        return pairs.pop()
    
run_program = Solution()
print(run_program.singleNumber([2,2,1,3,3]))