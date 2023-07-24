def move_zeros_to_end(nums):
    n = len(nums)
    next_non_zero_idx = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[next_non_zero_idx] = nums[next_non_zero_idx], nums[i]
            next_non_zero_idx += 1
nums1 = list(map(int, input("Enter elements of the array separated by space: ").split()))
move_zeros_to_end(nums1)
print(nums1)
