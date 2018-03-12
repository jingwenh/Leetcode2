# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        
        nodes_set = set()
        nodes_map = dict()
        
        q = []
        q.append(node)
        
        while len(q) > 0:
            cur = q.pop(0)
            new_node = UndirectedGraphNode(cur.label)
            nodes_set.add(cur)
            nodes_map[cur] = new_node
            
            for n in cur.neighbors:
                if n not in nodes_set:
                    q.append(n)
        
        # print(node.neighbors)
        
        for old, new in nodes_map.items():
            for n in old.neighbors:
                new.neighbors.append(nodes_map[n])
        
        return nodes_map[node]
