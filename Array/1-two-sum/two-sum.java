class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        int[] out = {-1, -1};
  
        for(int i=0;i<nums.length;i++) {
            if(map.containsKey(target-nums[i])) {
                out[0] = map.get(target-nums[i]);
                out[1] = i;
            }
            map.put(nums[i], i);
        }
        return out;
    }
}