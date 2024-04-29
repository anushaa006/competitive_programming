class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst=[ ]
        for i in range (2**n):
            j=i^(i>>1)
            lst.append(j)
        return lst