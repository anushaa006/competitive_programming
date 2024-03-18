class Solution(object):
    def kthSmallest(self, matrix, k):
        seen=[]
        for i in range (len(matrix)):
            for j in range(len(matrix)):
                seen.append(matrix[i][j])
        seen.sort()
        return seen[k-1]
        