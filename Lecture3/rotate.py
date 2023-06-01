nums = [1,2,3,4,5,6,7]
k = 3

count = 0
if len(nums)//2 > k :
    while count < k:
        pop = nums.pop(-1)
        nums.insert(0,pop)
        count += 1

elif len(nums)//2 <= k:
    while count < k:
        pop = nums.pop(0)
        nums.insert(-1,pop)
        count += 1