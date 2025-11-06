class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0 
        right = len(height)-1
        maxvol=0

        while left< right:
            maxh = min(height[left],height[right])
            vol = maxh*(right-left)
            maxvol = max(vol,maxvol)

            if left<right:
                left+=1
            if right < left:
                right -=1

        return maxvol