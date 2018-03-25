# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:48:42 2018

@author: Lenovo
"""

class Solution:
    def Power(self, base, exponent):
        result = 1
        for i in range(exponent):
            result = result * base
        return result
    def fast_power(self, base, exponent):
        if base == 0:
            return 0 
        if exponent == 0:
            return 1
        e = abs(exponent)
        tmp = base
        res = 1
        while(e > 0):
            #如果最后一位为1，那么给res乘上这一位的结果
            if (e & 1 == 1):
                res *= tmp
            e = e >> 1
            tmp *= tmp
        return res if exponent > 0 else 1/res
    
if __name__ == "__main__":
    solution = Solution()
#    result = solution.Power(2.4,3)
    result = solution.fast_power(2.4,13)
    print(result)
#    pow(2,2)