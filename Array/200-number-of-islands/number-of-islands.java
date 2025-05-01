class Solution {

    private int ROWS;
    private int COLS;
    private Set<String> visited;
    private char[][] grid;

    public  void dfs(int r, int c) {
        visited.add(r+"_"+c);
        int[][] dirs = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        for(int[] dir : dirs ) {
            int new_r = dir[0] + r;
            int new_c = dir[1] + c;

            if(0<=new_r && new_r< ROWS && 0<=new_c && new_c< COLS && !visited.contains(new_r+"_" + new_c) && grid[new_r][new_c] == '1' ) {
                dfs(new_r, new_c);
            }
        }
    }

    public int numIslands(char[][] grid) {
        this.grid = grid;
        this.ROWS = grid.length;
        this.COLS = grid[0].length;
        this.visited = new HashSet<>();
       
        int islands = 0;
        for(int i=0;i<ROWS;i++) {
            for(int j = 0; j<COLS; j++) {
                if(grid[i][j] == '1' && !visited.contains(i+"_"+ j)) {
                    islands++;
                    dfs(i,j);
                }
            }
        }
        return islands;

        

    }
}