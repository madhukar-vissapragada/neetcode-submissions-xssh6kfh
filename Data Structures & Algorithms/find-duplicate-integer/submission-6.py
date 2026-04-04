class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0

        while index < len(nums):
            if nums[index] != index + 1:
                correct_index = nums[index] - 1

                if nums[index] == nums[correct_index]:
                    return nums[index]

                nums[index], nums[correct_index] = nums[correct_index], nums[index]
            else:
                index += 1