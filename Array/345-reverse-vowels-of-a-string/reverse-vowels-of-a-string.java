class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')) ;


        StringBuilder out = new StringBuilder(s);
        int r = out.length()-1;
        int l = 0;

        while(l<r) {
            if(!vowels.contains(out.charAt(l))) {
                l++;
            } else if(!vowels.contains(out.charAt(r))) {
                r--;
            } else {
                char temp = out.charAt(l);
                out.setCharAt(l,out.charAt(r));
                out.setCharAt(r, temp);
                l++;
                r--;
            }
           
        }

        return out.toString();
    }
}