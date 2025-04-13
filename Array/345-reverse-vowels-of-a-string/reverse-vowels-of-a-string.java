class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') ;


        // StringBuilder out = new StringBuilder(s);
        // int r = out.length()-1;
        // int l = 0;

        // while(l<r) {
        //     char leftChar = out.charAt(l);
        //     char rightChar = out.charAt(r);
        //     if(!vowels.contains(leftChar)) {
        //         l++;
        //     } else if(!vowels.contains(rightChar)) {
        //         r--;
        //     } else {
        //         out.setCharAt(l,rightChar);
        //         out.setCharAt(r, leftChar);
        //         l++;
        //         r--;
        //     }
           
        // }

        // return out.toString();


        char[] word = s.toCharArray();
        int r = word.length-1;
        int l = 0;

        while(l<r) {
            
            if(!vowels.contains(word[l])) {
                l++;
            } else if(!vowels.contains(word[r])) {
                r--;
            } else {
                char temp = word[l];
                word[l] = word[r];
                word[r] = temp;
                l++;
                r--;
            }
           
        }

        return new String(word);

    }
}