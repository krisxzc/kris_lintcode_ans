'''
二叉树的前、中、后序遍历

挑战：非递归实现

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""




######## 前序
#递归
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
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

        
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    #迭代
    #用栈
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            #入栈先右后左，则出栈先左后右
            if node.right:              
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    
    
    
    
###################中序后序只写了递归，有时间再考虑迭代        
########### 中序  
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    
    #递归
    def inorderTraversal(self, root):
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return []
        self.traverse(root.left)
        self.results.append(root.val)
        self.traverse(root.right)





################后序
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return []
        self.traverse(root.left)
        #self.results.append(root.val)
        self.traverse(root.right)
        self.results.append(root.val)




