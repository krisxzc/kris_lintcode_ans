'''
二叉树的前、中、后序遍历

挑战：非递归实现

'''



# 只写了递归实现

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    #'''
    #递归
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return []
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)  
