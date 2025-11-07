class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum =0
        prefix_count = {0:1}
        count=0

        for num in nums:
            prefix_sum += num
            if prefix_sum-k in prefix_count:
                count+= prefix_count[prefix_sum-k]
            prefix_count[prefix_sum] =prefix_count.get(prefix_sum,0)+1

        return count