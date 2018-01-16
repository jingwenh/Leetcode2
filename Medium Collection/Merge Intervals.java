/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
//先按照lower bound排序
//排完序按顺序两两merge
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        Queue<Interval> pq = new PriorityQueue<>(7, new IntervalComparator());
        for (Interval i : intervals) {
            pq.offer(i);
        }
        
        List<Interval> res = new ArrayList<>();
        while (!pq.isEmpty()) {
            if (pq.size() >= 2) {
                Interval i1 = pq.poll();
                Interval i2 = pq.poll();
                List<Interval> afterMerge = merge(i1, i2);
                //两个merge不了，说明第一个interval已经没有办法再merge了
                //把第一个interval放进res，第二个还有可能可以和第三个merge，所以放回pq
                //如果两个可以merge，得到的新的Interval还有可能和后面的merge，所以把新的interval放进pq
                if (afterMerge.size() == 2) {
                    res.add(afterMerge.get(0));
                    pq.offer(afterMerge.get(1));
                } else {
                    pq.offer(afterMerge.get(0));
                }
            } else {
                res.add(pq.poll());
            }
        }
        return res;
    }
    
    private class IntervalComparator implements Comparator<Interval> {
        public int compare(Interval i1, Interval i2) {
            return i1.start - i2.start;
        }
    }
    
    //能merge就返回一个Interval, 不能Merge返回两个
    private List<Interval> merge(Interval i1, Interval i2) {
        List<Interval> res = new ArrayList<>();
        if (i1.end < i2.start) {
            res.add(i1);
            res.add(i2);
        } else {
            Interval i = new Interval(Math.min(i1.start, i2.start), Math.max(i1.end, i2.end));
            res.add(i);
        }
        return res;
    }
}
