"""
给定一个二叉树，找出其最小深度。
二叉树的最小深度为根节点到最近叶子节点的距离。

给出一棵如下的二叉树:

       1
     /   \ 
   2      3
         /  \
        4    5  

这个二叉树的最小深度为 2
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    
    #自己写的，类似层次遍历和最大深度
    def minDepth(self, root):
        # write your code here
        dept = 0
        if root is None:
            return dept
        
        q = []
        q.append(root)
        
        while len(q) != 0:
            # 深度加1
            dept += 1 
            length = len(q)
            for i in range(length):
                r = q.pop(0)
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
                
                #若左右节点都不存在，那输出当前深度
                #关键是这行
                if r.left is None and r.right is None:
                    return dept    
        
        return dept
        
