class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index_i = 0
        for index_j in range(len(nums)):
        	if nums[index_j] <= 0:
        		nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
        		index_i += 1

        for index in range(index_i, len(nums)):
        	if abs(nums[index]) - 1 < len(nums) and nums[abs(nums[index]) - 1] > 0:
        		nums[abs(nums[index]) - 1] =  -nums[abs(nums[index]) - 1]

        for index in range(nums):
        	if nums[index] > 0:
        		return index + 1
        return len(nums) + 1
