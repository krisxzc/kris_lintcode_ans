########### 两数之和
'''
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

你可以假设只有一组答案。

给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].

挑战：
O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here










########### 三数之和
'''
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

在三元组(a, b, c)，要求a <= b <= c。
结果不能包含重复的三元组。

如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：
(-1, 0, 1)
(-1, -1, 2)
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here












######### 四数之和
'''
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

四元组(a, b, c, d)中，需要满足a <= b <= c <= d
答案中不可以包含重复的四元组。

例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：
(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here






