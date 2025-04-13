class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for(int num: nums){
            totalSum+= num;
        }
        int[] leftSum = new int[nums.length];

        for(int i=1;i<nums.length;i++) {
            leftSum[i] = nums[i-1] + leftSum[i-1];
        }
        System.out.println(Arrays.toString(leftSum));

        for(int i=0;i<nums.length;i++) {
            System.out.println("leftSum:" + leftSum[i]);
            System.out.println(totalSum - nums[i]);

            if(totalSum - nums[i] - leftSum[i] == leftSum[i] ) {
                return i;
            }
        }
        return -1;
    }
}