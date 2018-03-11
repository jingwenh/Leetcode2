# BFS
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = set()
        target = len(graph) - 1
        q = deque()
        q.append([0])
        while len(q) > 0:
            cur_path = q.pop()
            cur_pos = cur_path[-1]
            if cur_pos == target:
                res.add(tuple(cur_path))
                continue
            for node in graph[cur_pos]:
                next_path = list(cur_path)
                next_path.append(node)
                q.append(next_path)
        return list(res)
