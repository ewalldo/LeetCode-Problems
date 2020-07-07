class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining_list = nums[i+1:]
            for j in range(len(remaining_list)):
                if (nums[i] + remaining_list[j] == target):
                    return [i, i+j+1]
