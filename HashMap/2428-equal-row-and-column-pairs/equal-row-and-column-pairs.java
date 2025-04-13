class Solution {
    public int equalPairs(int[][] grid) {
        
        int n = grid.length;

        int count = 0;
        for (int i=0;i<n;i++) {
            int[] row = grid[i];
            for (int k=0;k<n;k++) {
                int[] col = new int[n];

                for(int j = 0; j<n;j++) {
                    col[j] = grid[j][k];
                }
                
                if(Arrays.equals(col, row)) {
                    count++;
                }
            }
            

           
        }
        return count;
    }
}