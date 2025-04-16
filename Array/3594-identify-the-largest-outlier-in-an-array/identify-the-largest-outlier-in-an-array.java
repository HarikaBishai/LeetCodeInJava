class Solution {
    public int getLargestOutlier(int[] nums) {
        Map <Integer, Integer> map = new HashMap<>();
        int totalSum = 0;
        for(int num: nums) {
            totalSum+=num;
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int maxOut = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++) {
            int sum = 2*nums[i];
            int out = totalSum - sum;

            if(map.containsKey(out) && (out!=nums[i] || map.get(out) > 1)) {
                maxOut = Math.max(out, maxOut);
            }
        }
        return maxOut;
    }
}