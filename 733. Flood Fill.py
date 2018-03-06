class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        delta = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        q = []
        s = set()
        q.append((sr, sc))
        while len(q) > 0:
            cur = q.pop()
            if cur in s:
                continue
            s.add(cur)
            image[cur[0]][cur[1]] = newColor
            for d in delta:
                next = (cur[0] + d[0], cur[1] + d[1])
                if (next[0] >= 0 and next[0] < len(image) 
                    and next[1] >= 0 and next[1] < len(image[0]) 
                    and image[next[0]][next[1]] == oldColor):
                    q.append(next)
        return image
