class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int l = 0;
        double maxAvg = Double.NEGATIVE_INFINITY;

        int currSum = 0;

        for(int r=0;r<nums.length;r++) {
            currSum += nums[r];
            if(r-l+1 > k) {
                currSum-=nums[l];
                l++;
            } 

            if (r-l+1 == k) {
                maxAvg = Math.max(maxAvg, (currSum)/((double) k));
            }


        }

        return maxAvg;
    }
}