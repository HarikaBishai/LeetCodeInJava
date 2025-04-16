class Solution {
    public int trap(int[] height) {
        

        Stack<Integer> stk = new Stack<>();
        int totalWater = 0;

        for(int i=0; i< height.length; i++) {
            while(!stk.isEmpty() && height[stk.peek()] < height[i]) {
                int curr = stk.pop();
                if(!stk.isEmpty()) {
                    int leftIndex = stk.peek();
                    int leftHeight = height[leftIndex];
                    int rightHeight =height[i];
                    totalWater += (i-leftIndex-1) * (Math.min(leftHeight,rightHeight) - height[curr]);

                }
            }
            stk.push(i);
        }

        return totalWater;
    }
}