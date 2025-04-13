class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')) ;


        StringBuilder out = new StringBuilder(s);
        int r = out.length()-1;
        int l = 0;

        while(l<r) {
            char leftChar = out.charAt(l);
            char rightChar = out.charAt(r);
            if(!vowels.contains(leftChar)) {
                l++;
            } else if(!vowels.contains(rightChar)) {
                r--;
            } else {
                out.setCharAt(l,rightChar);
                out.setCharAt(r, leftChar);
                l++;
                r--;
            }
           
        }

        return out.toString();
    }
}