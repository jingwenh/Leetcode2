class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            self.nums = nums
            self.prefix_sum = [0 for i in nums]
        else:
            self.nums = nums
            self.prefix_sum = [0 for i in nums]
            self.prefix_sum[0] = nums[0]

            for i in range(1, len(nums)):
                self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]
        
        # print(self.prefix_sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j] - self.prefix_sum[i] + self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
