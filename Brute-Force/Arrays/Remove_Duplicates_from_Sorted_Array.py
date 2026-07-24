class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []

        for num in nums:
            if num not in temp:
                temp.append(num)

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)