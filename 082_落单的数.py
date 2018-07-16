"""
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。
给出 [1,2,2,1,3,4,3]，返回 4

挑战：一次遍历，常数级的额外空间复杂度
"""

# 要点：位运算 异或运算^
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # 思路要点：一个数字和自己异或一次会变成0
        ans = 0;
        for x in A:
            ans = ans ^ x
        return ans
        # 全部连乘后用交换律，相同的数异或一次后变成0 
        
