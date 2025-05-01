class Solution {
    public int lengthOfLongestSubstring(String s) {

        int l = 0;
        int maxLength = 0;

        Map<Character, Integer> map = new HashMap<>();

        for(int r = 0;r<s.length();r++) {
            char key = s.charAt(r);
            while(map.containsKey(key) && l<r) {
                map.put(s.charAt(l), map.get(s.charAt(l))-1);
                if(map.get(s.charAt(l)) == 0) {
                    map.remove(s.charAt(l));
                }
                l++;
            }

            map.put(key, map.getOrDefault(key, 0)+1);
            maxLength = Math.max(maxLength, r-l+1);
        }
        return maxLength;
        
    }
}