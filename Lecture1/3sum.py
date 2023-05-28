from typing import List


class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] <= 0:
                temp_nums = nums[i+1:]
                l = 0
                r = len(temp_nums) - 1
                while l < r:
                    if temp_nums[l] + temp_nums[r] + nums[i] == 0:
                        if [nums[i], temp_nums[l], temp_nums[r]] not in triplets:
                            triplets.append([nums[i], temp_nums[l], temp_nums[r]])
                        l += 1
                        r -= 1
                    elif temp_nums[l] + temp_nums[r] + nums[i] > 0:
                        r = r - 1
                    elif temp_nums[l] + temp_nums[r] + nums[i] < 0:
                        l += 1
        return triplets

if __name__ == '__main__':
    sol = Solution()
    nums =  [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))
