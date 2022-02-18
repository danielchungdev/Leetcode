class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            if (target - nums[i] not in seen):
                seen[nums[i]] = i
            else:
                print(nums[i])
                return [i, seen[target - nums[i]]]
