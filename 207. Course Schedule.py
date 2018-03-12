class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree_map = {}
        for t in prerequisites:
            course = t[0]
            pre = t[1]
            if course in indegree_map:
                indegree_map[course] = indegree_map[course] + 1
            else:
                indegree_map[course] = 1
        
        q = []
        for i in range(numCourses):
            if i not in indegree_map:
                q.append(i)
        
        count = 0
        while len(q) > 0:
            cur = q.pop(0)
            count = count + 1
            for course in prerequisites:
                if course[1] == cur:
                    indegree_map[course[0]] = indegree_map[course[0]] - 1
                    if indegree_map[course[0]] == 0:
                        q.append(course[0])
        
        if count == numCourses:
            return True
        else:
            return False
            
        
