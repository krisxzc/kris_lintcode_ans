"""
写一个程序来检测一个整数是不是丑数。
丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。
#可以认为 1 是一个特殊的丑数。

给出 num = 8，返回 true。
给出 num = 14，返回 false。
"""

# 想法比较重要
# 除到不能被那几个数整除之后，剩下1的就是丑数，剩下不是1的说明还有其他质因子


class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num):
        # write your code here
        if num <= 0:
            return False
        if num == 1:
            return True  
          
        while num >= 2 and num % 2 == 0:
            num //= 2;                          # /是浮点数除法  //是整数除法
        while num >= 3 and num % 3 == 0:
            num //= 3;  
        while num >= 5 and num % 5 == 0:
            num //= 5;  
          
        return num == 1
