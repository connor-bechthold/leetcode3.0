class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, right = 0, n - 1
        top, bottom = 0, n - 1

        while left < right and top < bottom:

            for i in range(right - left):

                # top left to top right
                temp_one = matrix[top + i][right]
                matrix[top + i][right] = matrix[top][left + i]

                # top right to bottom right
                temp_two = matrix[bottom][right - i]
                matrix[bottom][right - i] = temp_one

                # bottom right to bottom left
                temp_three = matrix[bottom - i][left]
                matrix[bottom - i][left] = temp_two

                # bottom left to top left
                matrix[top][left + i] = temp_three

            top += 1
            left += 1
            bottom -= 1
            right -= 1
