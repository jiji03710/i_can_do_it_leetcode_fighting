class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [i, hashmap[target-nums[i]]]
            if nums[i] in hashmap:
                continue
            else:
                hashmap[nums[i]] = i