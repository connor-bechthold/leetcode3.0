class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sol = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # left to right
            for i in range(left, right):
                sol.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom):
                sol.append(matrix[i][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                return sol

            # right to left
            for i in range(right - 1, left - 1, - 1):
                sol.append(matrix[bottom - 1][i])
            bottom -= 1

            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                sol.append(matrix[i][left])
            left += 1

        return sol
