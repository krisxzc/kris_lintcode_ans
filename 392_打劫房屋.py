"""
假设你是一个专业的窃贼，准备沿着一条街打劫房屋。
每个房子都存放着特定金额的钱。
你面临的唯一约束条件是：
#####相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。#######

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

给定 [3, 8, 4], 返回 8.

挑战：
O(n) 时间复杂度 且 O(1) 存储。

"""

#动态规划
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    
    # 自己写的一个很慢的解法
    def houseRobber(self, A):
        if len(A) == 0:
            return 0 
        if len(A) == 1:
            return A[0]
        dp = [0] * len(A)
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])
        if len(A) >= 2:
            for i in range(2, len(A)):
                dp[i] = max(dp[i-1], dp[i-2] + A[i])
        return dp[-1]
        
        
