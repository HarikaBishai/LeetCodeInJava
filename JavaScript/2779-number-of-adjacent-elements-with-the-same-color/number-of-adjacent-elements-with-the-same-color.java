class Solution {
    public int[] colorTheArray(int n, int[][] queries) {
        

        int[] colored = new int[n];
        int[] out = new int[queries.length];
        int j = 0;
        int count = 0;
        for (int[] q: queries) {
            int idx = q[0];
            int color = q[1];
            
            if(idx>0 && colored[idx]!=0 && colored[idx]==colored[idx-1]) {
                count--;
            }
            if(idx<n-1 && colored[idx]!=0 && colored[idx]==colored[idx+1]) {
                count--;
            }
            colored[idx] = color;
            if(idx>0 && colored[idx]==colored[idx-1]) {
                count++;
            }

            if(idx<n-1 &&  colored[idx]==colored[idx+1]) {
                count++;
            }
            out[j++] = count;
            
        }
        return out;
    }
}