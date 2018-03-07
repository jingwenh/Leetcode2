# Count maximum distances of all number in nums with the greatest frequency
from collections import Counter
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degree = Counter(nums).most_common(1)[0][1]
        
        num_to_indexes = {}
        for i, num in enumerate(nums):
            if num in num_to_indexes:
                num_to_indexes[num].append(i)
            else:
                num_to_indexes[num] = [i]
        
        distances = []
        for key, value in num_to_indexes.items():
            if len(value) == degree:
                distances.append(value[-1] - value[0] + 1)
        
        return min(distances)
        
