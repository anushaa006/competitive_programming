class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum+=nums[i]
        maxSum = sum
        start  = 0
        end = k
        while end < (len(nums)):
            sum = sum - nums[start]
            start+=1

            sum = sum+ nums[end]
            end+=1

            maxSum = max(sum, maxSum)
        return maxSum/k