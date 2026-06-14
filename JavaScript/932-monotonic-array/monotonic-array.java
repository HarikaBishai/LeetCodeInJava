class Solution {

    int[] nums;

    public boolean isMonotonic(int[] nums) {
        this.nums = nums;
        return isMonotonicallyIncreasing() || isMonotonicallyDecreasing();
    }

    public boolean isMonotonicallyIncreasing() {
        for (int i= 1;i<nums.length;i++) {
            if(nums[i-1] > nums[i]){
                return false;
            }
        }
        return true;
    }

    public boolean isMonotonicallyDecreasing() {
        for (int i= 1;i<nums.length;i++) {
            if(nums[i-1] < nums[i]){
                return false;
            }
        }
        return true;
    }
 }