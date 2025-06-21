class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)

        for i in range(ROWS):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        for i in range(ROWS):
            for j in range(ROWS//2):
                matrix[i][j], matrix[i][ROWS-j-1] = matrix[i][ROWS-j-1],  matrix[i][j]