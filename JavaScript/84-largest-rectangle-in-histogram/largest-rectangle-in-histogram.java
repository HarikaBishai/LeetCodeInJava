class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stk = new Stack<>();
        int max_area = 0;
        int n = heights.length;

        for(int i=0;i<=n;i++) {
            int currHeight = i == n ? 0 : heights[i];
            while(!stk.isEmpty() && heights[stk.peek()] > currHeight ) {
                int index = stk.pop();
                int left = stk.isEmpty() ? -1: stk.peek();
                int height = heights[index];
                int right = i;
                int width = right-left - 1;

                max_area = Math.max(max_area, height*width);

            }
            if(i < n) {
                stk.push(i);
            }
        }
        return max_area;
    }
}