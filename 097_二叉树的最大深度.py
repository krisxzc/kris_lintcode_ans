"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。


给出一棵如下的二叉树:
  1
 / \ 
2   3
   / \
  4   5
这个二叉树的最大深度为3.
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
    @param root: The root of binary tree.
    @return: An integer
    """
    
    #自己写的 用的方法类似T69树的层次遍历
    def maxDepth(self, root):
        # write your code here
        dept = 0
        if root is None:
            return dept
        
        q = []
        q.append(root)
        while len(q) != 0:
            length = len(q)
            for i in range(length):
                r = q.pop(0)
                
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
            dept += 1
        return dept   
