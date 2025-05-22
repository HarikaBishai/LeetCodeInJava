class Solution {

    private int ROWS;
    private int COLS;
    private Set<String> visited;
    private char[][] grid;

    public void dfs(int r, int c) {
        visited.add(r+"-"+c);
        int[][] dirs = {{0,-1}, {0, 1}, {-1,0}, {1,0}};

        for(int[] dir: dirs) {
            int new_r = r + dir[0];
            int new_c = c + dir[1];

            if(new_r>=0 && new_r<ROWS && new_c>=0 && new_c<COLS && grid[new_r][new_c] == '1' && !visited.contains(new_r + "-" + new_c)) {
                dfs(new_r, new_c);
            }

        }
    }

    public int numIslands(char[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        visited = new HashSet<>();
        this.grid = grid;
        int islandsCount = 0;

        for(int i=0;i<ROWS; i++) {
            for(int j=0;j<COLS;j++) {
                if(grid[i][j] == '1' && !visited.contains(i+"-" + j)) {
                    dfs(i,j);
                    islandsCount++;
                }
            }
        }
        return islandsCount;
        


    }
}