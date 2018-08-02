
"""
Run Code Status: Time Limit Exceeded
-------
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        maxV = 0
        while (height[i]):
            j = i + 1;
            while (height[j]):
                value = abs(i - j) * min(height[i],height[j])
                if(value > maxV):
                    maxV = value
        
        return maxV
"""

# untime: 32 ms
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        maxV = -1
        j = len(height) - 1;
        while (i < j):
            maxV = max(maxV,(j - i) * min(height[i],height[j]))
            if(height[i] < height[j]):
                i+=1;
            else:
                j-=1;
        return maxV