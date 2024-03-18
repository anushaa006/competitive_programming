class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        count=0
        for i in range(0,len(nums),2):
            count+=nums[i]
        return count