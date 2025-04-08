#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        # Step 1: Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Step 2: Fill remaining positions with 0
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums) # output [1,3,12,0,0]