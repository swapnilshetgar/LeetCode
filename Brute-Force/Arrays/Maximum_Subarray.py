class Solution(object):
    def maxSubArray(self, nums):
        current = 0
        maximum = nums[0]

        for i in range( len(nums)):
            
		current+=nums[i]
		if current >maximum:
			maximum=current
		if current<0:
			current=0
        return maximum