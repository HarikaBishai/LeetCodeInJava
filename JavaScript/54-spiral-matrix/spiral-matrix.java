class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> order = new ArrayList<>();

        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        int top = 0;
        int bottom = ROWS-1;
        int left = 0;
        int right = COLS - 1;

        while(top <= bottom && left<=right) {
            for(int c=left;c<=right; c++) {
                order.add(matrix[top][c]);
            }
            top++;
            for(int r=top; r<=bottom;r++) {
                order.add(matrix[r][right]);
            }
            right--;

            if(top<=bottom) {
                for(int c=right; c>=left;c--) {
                    order.add(matrix[bottom][c]);
                }
                bottom--;
            }

            if(left<=right) {
                for(int r= bottom;r>=top;r--) {
                    order.add(matrix[r][left]);
                }
                left++;
            }
        }
        return order;
    }
}