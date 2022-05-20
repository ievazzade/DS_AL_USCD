def maximumPairwiseProduct(nums):
    '''Broute Force Approach
    '''
    n = len(nums)
    mpp = 0
    for i in range(n):
        for j in range(i+1, n):
            mpp = max(nums[i]*nums[j], mpp)
        
    return mpp

if __name__=='__main__':
    input_n = int(input())
    input_nums = [int(x) for x in input().split()]
    print(maximumPairwiseProduct(input_nums))
