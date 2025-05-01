class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b)-> a[0]-b[0]);

        Stack<int[]> stk = new Stack<>();

        for(int[] interval: intervals) {
            if(!stk.isEmpty() && stk.peek()[1] >= interval[0]) {
                int[] peek = stk.pop();
                interval[0] = peek[0];
                interval[1] = Math.max(peek[1], interval[1]);
            }

            stk.push(interval);
        }
        int[][] out = new int[stk.size()][];
        int i = stk.size()-1;

        while(i>=0) {
            out[i] = stk.pop();
            i--;
        }
        return out;

    }
}