class Solution:
    def removeDuplicates(self, nums):
        #index to insert new value.
        insertIndex = 1
        for i in range(len(nums)):
            #go to next item until a different number is found.
            if nums[i - 1] == nums[i]:
                #change the value at insertIndex with the value at current item
                nums[insertIndex] = nums[i]
                #change place to insert
                insertIndex += 1
        return insertIndex
