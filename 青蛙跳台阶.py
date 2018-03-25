# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 09:12:17 2018

@author: Lenovo
"""
#一只青蛙一次可以跳上1级台阶，也可以跳上2级。
#求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:

    def jumpFloor(self,number):
        util = [0,1,2]
        if number == 0:
            return util[0]
        elif number == 1:
            return util[1]
        elif number == 2:
            return util[2]
        #当number = 3,4,5,6...时进入下面的for循环
        for i in range(3,number+1):
            util.append(util[i-1] + util[i-2])
        return util[-1]

    def jumpFloorII(self, number):
        # write code here
        util = [0,1,2]
        if number == 0:
            return util[0]
        elif number == 1:
            return util[1]
        elif number == 2:
            return util[2]
        #当number = 3,4,5,6...时进入下面的for循环
        for i in range(3,number+1):
            tmp = 0
            for j in range(1,i):
                tmp += util[i-j]
            util.append(tmp + 1)
        return util[-1]        

if __name__ == "__main__":
    solution = Solution()
#    result = solution.jumpFloor(3)
    result = solution.jumpFloorII(4)
    print(result)