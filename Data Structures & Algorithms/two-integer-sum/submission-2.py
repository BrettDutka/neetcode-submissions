class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            for j in range(1, len(nums)):
                if nums[index] + nums[j] == target and index != j:
                    return [index, j]