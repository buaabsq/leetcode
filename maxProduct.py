def maxProduct(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        """
        dp_max代表，到第i个数为止，且以该数作为结尾的最大值，因此其最大值就是整个问题的最大值
        dp_min表示，到第i个数为止，且以该数结尾的最小值，
        若nums一直为正，那与max数组一致，若有负数，将会有变化
        最大值变化有两种情况，一种是前面是正值，接下来为正，那直接乘就是新的最大值
        另一种是前面是负数，接下来为负，负负得正
        当正负相异时
        dp_min[i] = dp_max[i-1]*nums[i]
        dp_max[i] = nums[i]
        因此整理情况：
        dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i]*nums[i])
        dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i]*nums[i])
        """
        dp_max = [0 for i in range(len(nums))]
        dp_min = [0 for i in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
        return max(dp_max)


if __name__ == "__main__":
    nums = [-2,3,-4]
    print(maxProduct(nums))
