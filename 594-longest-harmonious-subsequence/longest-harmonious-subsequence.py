class Solution(object):
    def findLHS(self, nums):
        num_counts={}
        for num in nums:
            num_counts[num]=num_counts.get(num,0) +1
        max_length=0
        for num in num_counts:
            if num+1 in num_counts:
                max_length=max(max_length,num_counts[num]+num_counts[num+1])
        return max_length