# 先sort
# 然后找重复元素
# 删掉重复元素
# 然后找缺哪个
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        left = 0
        right = 1
        dup = None
        while right < len(nums):
            if nums[left] == nums[right]:
                dup = nums[left]
                del nums[left]
                break
            left = left + 1
            right = right + 1
        
        if nums[0] != 1:
            return [dup, 1]
        if nums[-1] != len(nums) + 1:
            return [dup, len(nums) + 1]
        
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] - nums[left] == 2:
                return [dup, int((nums[right] + nums[left]) / 2)]
            left = left + 1
            right = right + 1        
        return None
