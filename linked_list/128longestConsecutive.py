class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        hashmap={}
        
        max_length = 0

        for num in nums:
            if num in hashmap:
                continue

            left_length = hashmap.get(num - 1, 0)
            right_length = hashmap.get(num + 1, 0)

            total_length = right_length + 1 + left_length

            max_length = max(total_length, max_length)

            hashmap[num]=total_length
            hashmap[num - left_length] =total_length
            hashmap[num + right_length] =total_length

        return max_length
