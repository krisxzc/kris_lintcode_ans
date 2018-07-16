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
        # 普通双循环方法
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
        return [-1, -1]

    
    
        # 哈希法
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]], i]
            hash[numbers[i]] = i
        #无解的情况
        return [-1, -1]









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
        # 最笨的方法 3次循环 还要排序 去重
        numbers.sort()
        length = len(numbers)
        temp = []
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if numbers[i] + numbers[j] + numbers[k] == 0:
                        temp.append([numbers[i], numbers[j], numbers[k]])
        
        # 去重
        result = []    
        for i in temp:
            if i not in result:
                result.append(i)
        return result

           
        
        # 还可以优化
        
        # 九章的解法
        '''
        题意：求数列中三个数之和为0的三元组有多少个，需去重
        暴力枚举三个数复杂度为O(N^3)
        先考虑2Sum的做法，假设升序数列a，对于一组解ai,aj, 另一组解ak,al 
        必然满足 i<k j>l 或 i>k j<l, 因此我们可以用两个指针，初始时指向数列两端
        指向数之和大于目标值时，右指针向左移使得总和减小，反之左指针向右移
        由此可以用O(N)的复杂度解决2Sum问题，3Sum则枚举第一个数O(N^2)
        使用有序数列的好处是，在枚举和移动指针时值相等的数可以跳过，省去去重部分
        '''
    def threeSum(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res









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
    #九章的解法
    # 多枚举一个数后，参照3Sum的做法，O(N^3) 
    def fourSum(self, numbers, target):
        # write your code here
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res   





