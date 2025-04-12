class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder s = new StringBuilder();


        int w1Length = word1.length();
        int w2Length = word2.length();
        int minLength = Math.min(w1Length, w2Length);

        int i = 0;

        while(i<minLength) {
            s.append(word1.charAt(i));
            s.append(word2.charAt(i));
            i++;
        }

        if(i<w1Length) {
            s.append(word1.substring(i, w1Length));
        }

        if(i<w2Length) {
            s.append(word2.substring(i, w2Length));
        }

        return s.toString();
    }
}