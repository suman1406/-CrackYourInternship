from typing import List
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)       
        column = len(matrix[0])
        
        rows = [False] * row
        cols = [False] * column

        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for i, r in enumerate(rows):
            if r:
                for c in range(column):
                    matrix[i][c] = 0
        for i, c in enumerate(cols):
            if c:
                for r in range(row):
                    matrix[r][i] = 0