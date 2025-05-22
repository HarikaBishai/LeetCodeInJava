class Solution {
    public int[][] merge(int[][] intervals) {
        Stack<int[]> stk = new Stack<>();

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        for(int[] interval: intervals) {

            if(!stk.isEmpty() && stk.peek()[1] >= interval[0]) {
                int[] peek = stk.pop();
                stk.push(new int[] {peek[0], Math.max(interval[1], peek[1])});
            }
            else {
                stk.push(interval);
            }
        }

        int[][] out = new int[stk.size()][2];
        int i = stk.size()-1;
        while(!stk.isEmpty()){
            out[i--] = stk.pop();
        }

        return out;
    }
}