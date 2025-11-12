class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = len(nums)
        product = [1]*x

        for n in range(len(nums)):
            if n>0:
                product[n] = product[n-1]*nums[n-1]
        
        suffix_product = 1 
        for i in range(len(nums)-1,-1,-1): #起始?（包含） ?束?（不包含） ??
            product[i] = product[i]*suffix_product
            suffix_product*= nums[i]
        return product
