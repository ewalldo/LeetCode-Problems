class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left):
            low = 0
            high = len(nums)

            while low < high:
                middle = (low + high) // 2

                if nums[middle] > target or (left and target == nums[middle]):
                    high = middle
                else:
                    low = middle + 1
            return low
        
        left_idx = binary_search(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, binary_search(nums, target, False)-1]
