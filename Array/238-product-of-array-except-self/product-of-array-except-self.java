class Solution {
    public int[] productExceptSelf(int[] nums) {
        

        int[] out = new int[nums.length];
        
        Arrays.fill(out, 1);

        int leftProduct = 1;

        for(int i=1;i<nums.length;i++) {
            leftProduct *= nums[i-1];
            out[i] = leftProduct;
        }

        int rightProduct = 1;

        for(int i=nums.length-2;i>=0;i--) {
            rightProduct *= nums[i+1];
            out[i] *= rightProduct;
        }

        return out;


    }
}