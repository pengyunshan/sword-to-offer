# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 12:14:44 2018

@author: Lenovo
"""

# =============================================================================
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
# =============================================================================
class Solution:
    def NumberOf1(self, n):
        # write code here
        numberof1 = 0
        if n == 0:
            return 0
        elif n > 0:
            while(n != 0):
                if(n%2 == 1):
                    numberof1 += 1
                n = n // 2
            return numberof1
        
        else:
            return bin(2**32-n).count('1')
    #一个负整数（或原码）与其补数（或补码）相加，和为模。
#    def Numberof1II(self, n):
#        return bin(n).count('1') if n > 0 else bin(2**32-n).count('1')
if __name__ == "__main__":
    solution = Solution()
#    result = solution.NumberOf1(15)
    result = solution.NumberOf1(-5)
#    result = solution.NumberOf1(5)
    print(result)

            