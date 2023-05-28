from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        c_max = c_min = result = nums[0]

        for num in nums[1:]:
            t_min = min(num, num*c_max, num*c_min)
            c_max = max(num, num*c_max, num*c_min)
            c_min = t_min
            result = max(c_max, result)

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,-2,4,-2]
    print(sol.maxProduct(nums))