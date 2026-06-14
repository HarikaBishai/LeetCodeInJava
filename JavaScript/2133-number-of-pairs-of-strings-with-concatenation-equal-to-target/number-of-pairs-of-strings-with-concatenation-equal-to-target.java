class Solution {
    public int numOfPairs(String[] nums, String target) {
        Map<String, Integer> freq = new HashMap<>();


        for(String s: nums) {
            freq.put(s, freq.getOrDefault(s, 0)+1);
        }

        int count = 0;

        for(String s: nums) {
            if(target.startsWith(s)) {
                String rem = target.substring(s.length());

                count+= freq.getOrDefault(rem, 0);
                if(rem.equals(s)) {
                    count--;
                }
            }
            
        }
        return count;
    }
}