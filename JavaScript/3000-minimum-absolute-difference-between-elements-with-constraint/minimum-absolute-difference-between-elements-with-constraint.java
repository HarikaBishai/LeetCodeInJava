class Solution {
    public int minAbsoluteDifference(List<Integer> nums, int x) {
        TreeSet<Integer> s = new TreeSet<>();
        int ans = Integer.MAX_VALUE;

        for(int i = x;i<nums.size(); i++) {
            int curr = nums.get(i);
            s.add(nums.get(i-x));

            Integer floor = s.floor(curr);
            Integer ceil = s.ceiling(curr);

            if(floor!=null) {
                ans = Math.min(ans, Math.abs(curr - floor));
            }
            if(ceil!=null) {
                ans = Math.min(ans, Math.abs(curr - ceil));
            }
        }

        return ans;
    }
}