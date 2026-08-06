class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        start=1

        for i in range(2,n):
            if i>=2:
                print(n) 

            if nums[start-1]!=nums[i]:
                start+=1
                nums[start],nums[i]=nums[i], nums[start]
        return start+1