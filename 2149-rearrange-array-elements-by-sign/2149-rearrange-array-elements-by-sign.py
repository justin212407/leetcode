class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        negative = 1
        positive = 0
        res= [0]*n
        for i in range(n):
            if(nums[i] > 0):
                res[positive] = nums[i]
                positive = positive + 2
            else: 
                res[negative] = nums[i]
                negative = negative + 2
        return res
        