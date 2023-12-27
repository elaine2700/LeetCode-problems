class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        for i in range(len(nums)):
            print(nums)
            print(i)
            print(pointer)

            if i == pointer and nums[i] != val:
                pointer = pointer + 1
                continue 

            if nums[i] == nums[pointer]:
                continue   

            print('equal')  
            if i != pointer and pointer < len(nums):
                print("Swap")
                temp = nums[i]
                nums[i] = nums[pointer]
                nums[pointer] = temp
                pointer = pointer + 1
                
            continue     
                
        print(nums)  
        return pointer

program_run = Solution()
print(program_run.removeElement([0,1,2,2,3,0,4,2], 2))