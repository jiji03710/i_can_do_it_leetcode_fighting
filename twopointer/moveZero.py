class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroindex = -1
        for i in range(len(nums)):
            if nums[i]!= 0 and zeroindex ==-1:
                continue
            if nums[i]==0 and zeroindex == -1:
                zeroindex = i
            if nums[i]!=0 and zeroindex!= -1:
                nums[zeroindex] = nums[i]
                nums[i]=0
                zeroindex = zeroindex+1
        return nums