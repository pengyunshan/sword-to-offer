# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:04:03 2018

@author: Lenovo
"""
# =============================================================================
# 
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变
# =============================================================================
class Solution:
    def reOrderArray(self, array):
        #需要一个辅助变量记录左边奇数数组最后的index
        odd_index = -1
        for i in range(len(array)):
            #如果这一位是奇数的话,odd_index到这个奇数之间的偶数向右移动一位
            #然后这个奇数查到odd_index+1的位置，odd_index += 1
            if array[i] & 1 == 1:
                tmp = array[i]
                #注意移动偶数的时候是从后向前逐个移动的
                for j in range(i-1, odd_index,-1):
                    array[j+1] = array[j]
                array[odd_index + 1] = tmp
                odd_index += 1
        return array

if __name__ == "__main__":
    solution = Solution()
    array = [5,4,3,2,1]
    new_array = solution.reOrderArray(array)
    print(new_array)