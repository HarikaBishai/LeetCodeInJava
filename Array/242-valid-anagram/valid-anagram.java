class Solution {
    public boolean isAnagram(String s, String t) {

        char[] sortedS = s.toCharArray();
        char[] sortedT = t.toCharArray();

        Arrays.sort(sortedS);
        Arrays.sort(sortedT);


        return Arrays.equals(sortedS, sortedT);
    }
}