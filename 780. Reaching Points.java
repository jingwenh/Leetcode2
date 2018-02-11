//BFS：TLE
//用堆做宽搜，根据x + y做排序
//当堆顶元素的x + y > tx + ty时结束宽搜，返回false
//如果中途达到了target, 返回true
class Solution {
    private class Coordinate {
        int x;
        int y;
        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
        boolean equals(Coordinate c) {
            if (this.x == c.x && this.y == c.y) {
                return true;
            } else {
                return false;
            }
        }
    }
    
    private class CoordinateComparator implements Comparator<Coordinate> {
        public int compare(Coordinate c1, Coordinate c2) {
            return (c1.x + c1.y - c2.x - c2.y);
        }
    }
    
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        PriorityQueue<Coordinate> q = new PriorityQueue<>(7, new CoordinateComparator());
        q.offer(new Coordinate(sx, sy));
        Coordinate target = new Coordinate(tx, ty);
        while (!q.isEmpty()) {
            Coordinate c = q.poll();
            if (c.x + c.y > target.x + target.y) {
                return false;
            }
            if (c.equals(target)) {
                return true;
            }
            Coordinate next1 = new Coordinate(c.x, c.y + c.x);
            Coordinate next2 = new Coordinate(c.x + c.y, c.y);
            q.offer(next1);
            q.offer(next2);
        }
        
        return false;
    }
}
