# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:21:37 2018

@author: Lenovo
"""
# =============================================================================
# 
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 
# =============================================================================
class Solution:
    def rectCover(self, number):
        util = [0,1,2]
        if number == 0:
            return util[0]
        elif number == 1:
            return util[1]
        elif number == 2:
            return util[2]
        #当number >= 3的时候进入下面的循环
        for i in range(3, number+1):
            util.append(util[i-1] + util[i-2])
        return util[-1]
        # write code here
if __name__ == "__main__":
    solution = Solution()
    result = solution.rectCover(1)
    print(result)
    result = solution.rectCover(2)
    print(result)
    result = solution.rectCover(3)
    print(result)
    result = solution.rectCover(4)
    print(result)