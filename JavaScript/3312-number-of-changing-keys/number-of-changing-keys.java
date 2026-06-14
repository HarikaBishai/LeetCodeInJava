class Solution {
    public int countKeyChanges(String s) {
        int count = 0;



        for(int i=1; i<s.length(); i++) {
            if(Character.toLowerCase(s.charAt(i-1)) != Character.toLowerCase(s.charAt(i))) {
                count++;
            }
        }
        return count;
    }
}