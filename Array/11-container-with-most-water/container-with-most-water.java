class Solution {
    public int maxArea(int[] height) {
        
        int l = 0;
        int r = height.length-1;
        int maxWater = 0;

        while(l<r){
            maxWater = Math.max(Math.min(height[l], height[r]) * (r-l), maxWater);


            if(height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxWater;
    }
}