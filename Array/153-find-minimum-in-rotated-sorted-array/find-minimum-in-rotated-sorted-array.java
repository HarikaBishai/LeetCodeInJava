class Solution {
    public int findMin(int[] nums) {
        int ans = Integer.MAX_VALUE;

        int l =0;
        int r = nums.length-1;

        while(l<=r){
            int m = (l+r)/2;

            if(nums[l]<=nums[r]) {
                ans = Math.min(nums[l], ans);
                break;
            }

            if(nums[l]<=nums[m]) {
                ans = Math.min(nums[l], ans);
                l=m+1;
            } else {
                ans = Math.min(nums[m], ans);
                r=m-1;
            }
        }
        return ans;

    }
}