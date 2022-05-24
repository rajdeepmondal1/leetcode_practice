# 238 - Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums):
    """
    :param nums: Inputs a list of Integer
    :return: An Array with product of all the elements of nums except current nums.
    """
    # Initializing an empty array
    answer = [0] * (len(nums))

    # Let's take an example array [1, 2, 3, 4]
    # Prefix is 1
    # First Position - 1(Prefix) = 1
    # Second Position - 1(Prefix) * 1(Array(1st value)) = 1
    # Third Position - 1(Prefix) * 2(Array(2nd value)) = 2
    # Fourth Position - 2(Prefix) * 3(Array(3rd value)) = 6
    prefix = 1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    # Postfix is 1
    # Last Position - 1(Postfix) * 6(Array(3rd value)) = 6
    # Third Position - 4(Postfix) * 2(Array(3rd value)) = 8
    # Second Position - 12(Postfix) * 1(Array(2nd value)) = 12
    # First Position - 24(Postfix) * 1(Array(1st value)) = 24
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]
    # Answer is [24, 12 ,8, 6]
    return answer


print(productExceptSelf([1, 2, 3, 4]))
