problem description

'''
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2

挑战：如果数组中的整数个数超过了2^32，你的算法是否会出错？
'''

# 难点在于第一次出现

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid + 1
            # target小于或等于nums[mid]，都把范围缩小到[left,mid-1]
            # 因为target = nums[mid]时，可能不是第一次出现target
            else:
                right = mid - 1
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        return -1    

