nums = [1,3,2]

def nextPerm(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
        nums = nums[:i+1] + sorted(nums[i+1:])
    else:
        nums.sort()
    return nums


if __name__ == "__main__":
    print(nums)
    print(nextPerm(nums=nums))