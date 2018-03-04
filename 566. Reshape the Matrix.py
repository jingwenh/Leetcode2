class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums[0]) * len(nums) != r * c:
            return nums
        
        elements = []
        for row in nums:
            for n in row:
                elements.append(n)
        
        res = []
        cursor = 0
        while cursor < len(elements):
            res.append(elements[cursor:cursor+c])
            cursor = cursor + c
        
        return res
