class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if row[-1] >= target:
                return target in row
        return False
        