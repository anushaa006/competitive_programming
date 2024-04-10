class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lst_len = len(nums)
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(1, lst_len - k + 1):
            cur_sum += (nums[i + k - 1] - nums[i - 1])
            max_sum = max(cur_sum, max_sum)
        
        return max_sum / k