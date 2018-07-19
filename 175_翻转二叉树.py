"""
翻转一棵二叉树
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4

挑战
递归固然可行，能否写个非递归的？
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    '''
    # 递归方法
    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): 
            self.dfs(left)
        if (right!=None): 
            self.dfs(right)
    '''
            
    def invertBinaryTree(self, root):
        # write your code here
        self.inv(root)
    def inv(self, node):
        node.left,node.right = node.right,node.left  #左右互换
        if (node.right!=None):
            self.inv(node.right)
        if (node.left!=None): 
            self.inv(node.left)
    # 非递归暂时不管了
