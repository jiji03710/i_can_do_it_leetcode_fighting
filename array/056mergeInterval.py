class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x : x[0])
        output = []

        for interval in intervals:
            if not output or output[-1][1]<interval[0]:
                output.append(interval)
            else:
                output[-1][1]= max(output[-1][1],interval[1])
        return output