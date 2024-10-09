class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for i in range(n):
            for j in range(int(n/2)):
                        temp = matrix[i][j]
                        matrix[i][j] = matrix[i][n-j-1]
                        matrix[i][n-j-1] = temp
                