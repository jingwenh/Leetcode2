class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # key = restaurant, value = index
        dic1 = {}
        for i, r in enumerate(list1):
            dic1[r] = i

        dic2 = {} 
        for i, r in enumerate(list2):
            dic2[r] = i
        
        res = []
        for key, value in dic1.items():
            if key in dic2:
                res.append((abs(dic1[key] + dic2[key]), key))
        
        least_index_diff = heapq.nsmallest(1, res)[0][0]
        
        return [tpl[1] for tpl in res if tpl[0] == least_index_diff]
        
