class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u');
        int l = 0;
        int maxVowels = 0;
        int currVowels = 0;

        for(int r=0;r<s.length();r++) {
            if (vowels.contains(s.charAt(r))) {
                currVowels++;
            }

            if (r-l+1 > k) {
                if(vowels.contains(s.charAt(l))) {
                    currVowels--;
                }
                l++;
            }

            if(r-l+1 == k) {
                maxVowels = Math.max(maxVowels, currVowels);
            }
        }
        return maxVowels;


    }
}