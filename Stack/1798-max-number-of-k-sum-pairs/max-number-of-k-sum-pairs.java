class Solution {
    public int maxOperations(int[] nums, int k) {
        Map <Integer, Integer> map = new HashMap<>();
        int count = 0;
        for(int num: nums) {
            if(map.containsKey((k-num))) {
                count++;
                map.put(k-num, map.get(k-num)-1);
                if(map.get(k-num) == 0) {
                    map.remove(k-num);
                }
            } else {
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
        }

        return count;
    }
}