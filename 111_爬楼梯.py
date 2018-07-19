# 动态规划

"""
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法，返回 3
"""

# 思路：第n层，可以由第n-1和n-2层达到，所以到第n层的方法数等于到第n-1和n-2层的方法数相加，以此类推

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <=2:
            return n
        
        result = [1,2]
        for _ in range(n-2):  #把1、2去掉
            result.append(result[-2] + result[-1])
        return result[-1]
