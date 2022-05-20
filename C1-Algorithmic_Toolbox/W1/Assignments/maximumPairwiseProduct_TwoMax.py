def maximumPairwiseProduct(nums):
    '''Finding the two biggest numbers
    '''
    n = len(nums)
    max1_index = 0
    for i in range(n):
        if nums[i]>nums[max1_index]:
            max1_index = i
    
    max2_index = 0
    if max1_index == 0:
        max2_index = 1
    else:
        max2_index = 0

    for j in range(n):
        if (nums[j]> nums[max2_index] and j != max1_index):
            max2_index = j
    result = nums[max1_index]*nums[max2_index]
    
    return result


if __name__=='__main__':
    input_n = int(input())
    input_nums = [int(x) for x in input().split()]
    print(maximumPairwiseProduct(input_nums))
