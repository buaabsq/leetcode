def get_max_sum(nums):
    """
    设max_sum[i]到第i个为止最高金额，详见最高题解分析，即i-1个是否被偷并不影响之后的答案
    则max_sum[i] = max(max_sum[i-2] + nums[i], max_sum[i-1])
    """
    max_sum = [0 for i in range(len(nums))]
    max_sum[0] = nums[0]
    for i in range(1, len(nums)):
        max_sum[i] = max(max_sum[i-2] + nums[i], max_sum[i-1])
    print(max_sum)  
    return max(max_sum)

def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        # 0-n-1,1-n中最大的，因为0与n相邻
        return max(get_max_sum(nums[:-1]), get_max_sum(nums[1:]))

if __name__ == "__main__":
    nums = [1, 3, 1, 3, 100]
    print(rob(nums))
