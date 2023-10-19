class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        row = -1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break

        if row == -1:
            return False

        l, r = 0, cols - 1
        while l <= r:
            val = (l + r) // 2
            if matrix[row][val] < target:
                l = val + 1
            elif matrix[row][val] > target:
                r = val - 1
            else:
                return True

        return False