class Solution {
    public int equalPairs(int[][] grid) {
        
        int n = grid.length;

        int count = 0;

        Map<String, Integer> map = new HashMap<>();

        for(int[] row: grid) {
            String rowString = Arrays.toString(row);
            map.put(rowString, map.getOrDefault(rowString, 0)+1);
        }

        System.out.println(map);

        for(int i=0;i<n;i++) {
            int[] col = new int[n];
            for(int j=0;j<n;j++) {
                col[j] = grid[j][i];
            }
            String colString = Arrays.toString(col);
            count+= map.getOrDefault(colString, 0);
        }
        
        return count;
    }
}