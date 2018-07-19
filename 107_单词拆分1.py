"""
给出一个字符串s和一个词典，判断字符串s是否可以被空格切分成一个或多个出现在字典中的单词。

给出
s = "lintcode"
dict = ["lint","code"]
返回 true 因为"lintcode"可以被空格切分成"lint code"
"""


# 思路 动态规划

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        
        dp = [False] * (len(s)+1) 
        dp[0] = True  
        # n+1个，第一个true是为了应付字符串为空的情况
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
        return dp[-1]

    
    # 在leetcode可以AC，lintcode不行
