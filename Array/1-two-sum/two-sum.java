class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        int[] out = new int[2];
        int n = nums.length;
        for(int i=0;i<n;i++) {
            int num = nums[i];

            if(seen.containsKey(target-num)) {
                out[0] = seen.get(target-num);
                out[1] = i;
                return out;
            }

            seen.put(num, i);
        }
        out[0] = -1;
        out[1] = -1;
        return out;
    }
}