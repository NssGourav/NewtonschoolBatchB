def partition(nums, n):
    pivot = nums[0]
    i = 0  

    for j in range(1, n):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[0], nums[i] = nums[i], nums[0]
    return i + 1
  
