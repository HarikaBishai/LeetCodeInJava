class Solution {
    public int countSubstrings(String s) {
        int out = 0;

        int i = 0;
        while(i < s.length()) {

            int l = i;
            int r = i;

            while(l>=0 && r<s.length() && s.charAt(l) == s.charAt(r)) {
                l-=1;
                r+=1;
                out++;
            }

            l = i;
            r = i+1;

            while(l>=0 && r<s.length() && s.charAt(l) == s.charAt(r)) {
                l-=1;
                r+=1;
                out++;
            }
            i++;


        }
        return out;
        

    }
}