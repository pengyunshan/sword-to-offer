# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:18:29 2018

@author: Lenovo
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        mid = len(rotateArray) // 2
        print('最后:',rotateArray[-1],";中间:",rotateArray[mid])
        if rotateArray[mid] == rotateArray[-1] or rotateArray[mid] == rotateArray[0]:
            print(rotateArray)
            return min(rotateArray)
        
        if rotateArray[-1] > rotateArray[mid]:
            print(rotateArray[:mid+1])
            return self.minNumberInRotateArray(rotateArray[:mid+1])
        else:
            print(rotateArray[mid:])
            return self.minNumberInRotateArray(rotateArray[mid:])
        
        

if __name__ == "__main__":
    data = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,
            9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,
            2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,
            5448,5668,5706,5725,6300,6335]
    solution = Solution()
    result = solution.minNumberInRotateArray(data)
    print(result)