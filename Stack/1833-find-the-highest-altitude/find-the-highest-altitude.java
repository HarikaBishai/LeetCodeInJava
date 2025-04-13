class Solution {
    public int largestAltitude(int[] gain) {
        
        int last = 0;
        int max = 0;

        for(int alt: gain) {
            last += alt;
            max = Math.max(max, last); 
        }
        return max;
    }
}