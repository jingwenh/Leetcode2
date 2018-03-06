class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        pq = []
        for i, score in enumerate(nums):
            pq.append((score, i))
        
        pq = heapq.nlargest(len(pq), pq)
        
        # （score, 运动员编号）
        # pq中的index就是这个运动员的rank
        for rank, info in enumerate(pq):
            if rank == 0:
                nums[info[1]] = "Gold Medal"
            elif rank == 1:
                nums[info[1]] = "Silver Medal"
            elif rank == 2:
                nums[info[1]] = "Bronze Medal"
            else:
                nums[info[1]] = str(rank + 1)
        
        return nums
        
        
