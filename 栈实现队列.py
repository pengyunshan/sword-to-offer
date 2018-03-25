# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:57:07 2018

@author: Lenovo
"""

class Solution:
    def __init__(self,val =[]):
        self.a = val
        self.b = []
    def push(self, node):
        # write code here
        self.a.append(node)
        return self.a
    def pop(self):
        # return xx
        while len(self.a) > 0:
            self.b.append(self.a.pop())
        self.b.pop()
#        print(self.b)
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        return self.a
if __name__ == "__main__":
    solution = Solution([])
    solution.push(1)
    solution.push(2)
    solution.push(3)
    solution.push(4)
    solution.push(5)
#    print(a)
    a = solution.pop()
#    solution.pop()
    