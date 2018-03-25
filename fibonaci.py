# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:57:49 2018

@author: Lenovo
"""

class Solution:
    def Fibonacci(self, n):
        util = [0,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2,n):
                util.append(util[-1] + util[-2])
                
        return util[-1]+ util[-2]
    
    def Fibonacci_digui(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

if __name__ == "__main__":
    solution = Solution()
#    print( solution.Fibonacci(0))
#    print( solution.Fibonacci(1))
    print( solution.Fibonacci(2))
#    print( solution.Fibonacci(3))
#    print( solution.Fibonacci(4))
#    print( solution.Fibonacci(5))
#    print( solution.Fibonacci(6))
#    print( solution.Fibonacci(7))
#    print( solution.Fibonacci(8))
#    print( solution.Fibonacci(32))
    