class Solution {
    public int longestSubarray(int[] nums) {
        int l = 0;

        int currSum = 0;
        int maxOnes = 0;

        for(int r=0;r<nums.length;r++) {
            currSum += nums[r];
            if((r-l+1)-currSum > 1) {
                currSum-=nums[l];
                l++;
            }

            maxOnes = Math.max(maxOnes, currSum);
        }
        if(maxOnes == nums.length) {
            return maxOnes-1;
        }
        return maxOnes;
    }
}