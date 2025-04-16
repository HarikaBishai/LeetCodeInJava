class Solution {
    public int characterReplacement(String s, int k) {
        if(s.length() == 0) {
            return 0;
        }
        Map<Character, Integer> map = new HashMap<>();


        int l = 0;
        int maxLength = 0;
        for(int r = 0;r<s.length(); r++) {
            map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0)+ 1);

            while((r-l+1) - map.values().stream().mapToInt(Integer::intValue).max().orElse(0) > k){
                map.put(s.charAt(l), map.getOrDefault(s.charAt(l), 0)- 1);
                l++;

            }

            maxLength = Math.max(maxLength, r-l+1);
        }
        return maxLength;
    }
}