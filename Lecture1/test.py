import random

def findKthLargest(nums, k):
    # Use QuickSelect algorithm to find the kth largest element
    return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

def quickSelect(nums, left, right, k):
    # Partition the array using a random pivot
    pivotIndex = random.randint(left, right)
    pivotIndex = partition(nums, left, right, pivotIndex)

    # Recursively search in the partitioned subarray
    if pivotIndex == k:
        return nums[pivotIndex]
    elif pivotIndex < k:
        return quickSelect(nums, pivotIndex + 1, right, k)
    else:
        return quickSelect(nums, left, pivotIndex - 1, k)

def partition(nums, left, right, pivotIndex):
    pivotValue = nums[pivotIndex]
    nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
    storeIndex = left

    for i in range(left, right):
        if nums[i] < pivotValue:
            nums[i], nums[storeIndex] = nums[storeIndex], nums[i]
            storeIndex += 1

    nums[storeIndex], nums[right] = nums[right], nums[storeIndex]
    return storeIndex

nums = [-563, -2528, 48, -1687, 792, -492, 2594, 3340, 7907, 4288, -5304, 4106, -1737, 2837, 8528, 5006, 2155,
            -9852, 2090,
            -3515, 29, 8505, -3498, 4319, 6192, -6747, -1072, 2631, -4359, 8383, -8392, 1559, 8001, 6304, 8090, -422,
            -6852,
            -8460, 605, 3497, 4604, 3288, 7829, 5121, -5826, 1814, -227, -501, -710, 2943, 2482, -6798, -6516, -8759,
            34, 9654,
            9711, -9894, -5798, 2458, -9674, -393, 4752, 8330, -9403, 1243, 1778, 3316, 2929, -6165, 2840, 8885, 5157,
            6947,
            1448, 5890, 2463, 6187, -3432, 8035, -2157, -975, 3496, 8339, -1652, -7574, -2850, -3852, 3271, 9861, 3983,
            -4708,
            -4946, -3634, 3581, -5376, -4883, -1582, 934, 1215, 3178, 8518, -6124, -4346, 2925, -9470, -3240, 90, 6153,
            905,
            9481, -7208, 9188, 8772, -3837, 8595, -1016, 4359, -7696, -8751, -5613, -1083, -2069, 1789, 6101, 1179,
            -111,
            -4053, -771, 9045, 681, 128, 7560, -2644, -9734, 7655, -5511, -8970, -4823, -5848, 8218, -2271, -6422, 8907,
            -9554,
            776, -1908, 3646, 5619, -4880, -2932, 7730, 3861, 5150, -6156, -297, 2098, 3303, 9891, 9601, 3072, -4468,
            8721,
            9175, -9046, -7477, 1989, -475, -1883, -8988, -6861, -9071, 8181, -3131, -3860, -2682, -8811, 1065, 4785,
            -4590,
            -6654, -434, -2655, -2149, -9487, 808, 1350, 8968, -3962, -4807, -3566, 3893, 4174, -249, -7224, -3927,
            9591, 3390,
            5112, 5646, 7489, 9545, 1757, 4935, -7933, -3071, -9916, 8794, -7823, 6892, -2125, 5664, 5891, 5266, 7790]
k = 15
result = findKthLargest(nums, k)
print(result)  # Output: 5
