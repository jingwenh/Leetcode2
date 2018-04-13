class Solution:
    # 先sort
    # 然后再遍历一般，index为奇数就和前面的数交换
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse = True)
        for i in range(len(nums)):
            if i % 2 == 1:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
        
