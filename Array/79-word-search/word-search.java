class Solution {

    private int rows;
    private int cols;
    private char[][] board;
    private Set<String> visited;
    private String word;


    public boolean dfs(int r, int c, int i) {
        if(i > word.length()) return false;
        if(i==word.length()-1) return true;
        
        visited.add(r+"_" + c);

        int[][] dirs = {{-1,0}, {1,0}, {0,1}, {0,-1}};

        for(int[] dir: dirs) {
            int new_r = r + dir[0];
            int new_c = c + dir[1];

            if(0<=new_r && new_r < rows && 0<=new_c && new_c<cols && board[new_r][new_c]==word.charAt(i+1) && !visited.contains(new_r+"_" + new_c)) {
                if(dfs(new_r , new_c, i+1)) {
                    return true;
                }
            }
        }


        visited.remove(r+"_" + c);
        return false;
    }



    public boolean exist(char[][] board, String word) {
        this.rows = board.length;
        this.cols = board[0].length;
        this.board = board;
        this.word = word;
        this.visited = new HashSet<>();


    

        for(int i=0;i<rows;i++) {
            for(int j=0;j<cols;j++) {
                if(board[i][j] == word.charAt(0) && dfs(i, j, 0)){
                    return true;
                }
            }
        }

        return false;
    }
}