from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 

        while i < len(nums)-1:
            mini = min(nums[i:])
            if nums[i] > mini:
                temp = nums[i]
                idx = nums[i:].index(mini) + i
                if temp != mini:
                    nums[i] = mini
                    nums[idx] = temp
            i += 1

        return nums
    

nums = [2,1,0,1,1,2,0,2]
Solution().sortColors(nums)