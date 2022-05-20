import random
def maximumPairwiseProductFast(nums):

    n = len(nums)
    max1_index = 0
    for i in range(1, n):
        if nums[i]>nums[max1_index]:
            max1_index = i
    
    if max1_index == 0:
        max2_index = 1
    else:
        max2_index = 0


    for j in range(n):
        if (nums[j]> nums[max2_index] and j != max1_index):
            max2_index = j
    
    return nums[max1_index]*nums[max2_index]

def maximumPairwiseProduct(nums):
    n = len(nums)
    mpp = 0
    for i in range(n):
        for j in range(i+1, n):
            mpp = max(mpp, nums[i]*nums[j])
    
    return mpp

if __name__=='__main__':

    while True:
        n = int(random.randint(1,100)+2)
        smaple_nums = []
        for i in range(n):
            smaple_nums.append(int(random.random()*10000))
        if(maximumPairwiseProduct(smaple_nums) != maximumPairwiseProductFast(smaple_nums)):
            print(smaple_nums)
            print(maximumPairwiseProduct(smaple_nums))
            print(maximumPairwiseProductFast(smaple_nums))
            break
        print("Ok!")
 
    # input_n = int(input())
    # input_nums = [int(x) for x in input().split()]
    # print(maximumPairwiseProduct(input_nums))
