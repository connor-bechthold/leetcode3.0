class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]
        val = 1

        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while left < right and top < bottom:

            # left to right
            for i in range(left, right):
                matrix[top][i] = val
                val += 1
            top += 1

            # top to bottom
            for i in range(top, bottom):
                matrix[i][right - 1] = val
                val += 1
            right -= 1

            if top >= bottom or left >= right:
                return matrix

            # right to left
            for i in range (right - 1, left - 1, -1):
                matrix[bottom - 1][i] = val
                val += 1
            bottom -= 1

            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = val
                val += 1
            left += 1

        return matrix
