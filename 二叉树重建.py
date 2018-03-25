# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:17:04 2018

@author: Lenovo
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
def reConstructBinaryTree(self, pre, tin):
    # write code here
    if not pre  or not tin:
        return None
    root = TreeNode(pre[0])
    index = tin.index(pre[0])
    root.left = self.reConstructBinaryTree(pre[1:index+1],tin[0:index])
    root.right = self.reConstructBinaryTree(pre[index+1:],tin[index+1:])
    return root    
