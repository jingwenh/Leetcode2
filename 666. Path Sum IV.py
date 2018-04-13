# For node xy its left child is (x+1)(y*2-1) and right child is (x+1)(y*2)
# 用HashMap表示tree（key=前两位，value=后一位）, 然后根据递推公式找子节点traverse
class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.tree = dict()
        self.sums = []
        for n in nums:
            self.tree[str(n)[0:2]] = int(str(n)[-1])
        if "11" not in self.tree:
            return 0
        
        self.traverse("11", 0)
        return sum(self.sums)
        
    def traverse(self, root, presum):
        presum = presum + self.tree[root]
        
        left_key = str(int(root[0])+1) + str(2 * int(root[1]) - 1)
        right_key = str(int(root[0])+1) + str(2 * int(root[1]))
        
        if left_key not in self.tree and right_key not in self.tree:
            self.sums.append(presum)
            return
        
        if left_key in self.tree:
            self.traverse(left_key, presum)
        if right_key in self.tree:
            self.traverse(right_key, presum)
