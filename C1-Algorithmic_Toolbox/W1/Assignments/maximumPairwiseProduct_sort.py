def maximumPairwiseProduct(nums):
    '''Broute Force Approach
    '''
    n = len(nums)
    nums.sort()
        
    return nums[-1]* nums[-2]

if __name__=='__main__':
    input_n = int(input())
    input_nums = [int(x) for x in input().split()]
    print(maximumPairwiseProduct(input_nums))
