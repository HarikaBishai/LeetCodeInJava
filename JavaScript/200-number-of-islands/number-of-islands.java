class Solution {
    private int ROWS;
    private int COLS;
    private int islands = 0;
    private boolean[][] visited;
    private char[][] grid;
    public int numIslands(char[][] grid) {
        ROWS = grid.length;
        COLS = grid[0].length;
        this.grid = grid;

        visited = new boolean[ROWS][COLS];
        
        for(int i=0;i<ROWS;i++) {
            for(int j=0;j<COLS;j++) {
               
                if(this.grid[i][j] == '1' && !visited[i][j]) {
                    islands++;
                    dfs(i, j);
                }
            }
        }
        return islands;

    }

    public void dfs(int i, int j) {
        
        visited[i][j] = true;

        int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        for (int[] dir: directions){
            int new_r = i + dir[0];
            int new_c = j + dir[1];
           

            if(new_r >= 0 && new_r < ROWS && new_c >= 0 && new_c <COLS && !visited[new_r][new_c] && grid[new_r][new_c] == '1') {
                dfs(new_r, new_c);
            }
        }
    }
}