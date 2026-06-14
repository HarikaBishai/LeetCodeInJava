class Solution {
    public int[][] candyCrush(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        boolean changed = true;

        while (changed) {

            changed = false;
            for(int r = 0; r<m;r++){
                for(int c=0;c+2<n;c++){
                    int val = Math.abs(board[r][c]);
                    if(val!=0 && val == Math.abs(board[r][c+1]) && val == Math.abs(board[r][c+2])) {
                        changed = true;
                        board[r][c] = -val;
                        board[r][c+1] = -val;
                        board[r][c+2] = -val;
                    }
                }
            }

            for(int r = 0; r+2<m;r++){
                for(int c=0;c<n;c++){
                    int val = Math.abs(board[r][c]);
                    if(val!=0 && val == Math.abs(board[r+1][c]) && val == Math.abs(board[r+2][c])) {
                        changed = true;
                        board[r][c] = -val;
                        board[r+1][c] = -val;
                        board[r+2][c] = -val;
                    }
                }
            }


            for(int c=0;c<n;c++) {
                int writerow = m-1;

                for(int r=m-1; r>=0; r--) {
                    if(board[r][c] > 0) {
                        board[writerow][c] = board[r][c];
                        writerow--;
                    }
                }

                while(writerow>=0) {
                    board[writerow][c] = 0;
                    writerow--;
                }
            }
        }

        return board;

        
    }
}