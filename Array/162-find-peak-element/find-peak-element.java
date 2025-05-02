class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length == 1) {
            return  0;
        }

        if(nums[0] > nums[1]) {
            return 0;
        }

        int n = nums.length-1;

        if(nums[n] > nums[n-1]) {
            return n;
        }

        int l = 1;
        int r = n-1;

        while(l<=r) {
            int mid = (l+r)/2;

            if(nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1]) {
                return mid;
            }  
            if(nums[mid] < nums[mid+1]) {
                l = mid+1;
            } else {
                r=mid-1;
            }
        }
        return -1;
    }
}