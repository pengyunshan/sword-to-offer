# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 11:32:13 2018

@author: Lenovo
"""

N = input('')
N = int(N)
penny = [1,5,10,20,50,100]
matrix = [[0 for i in range(6)] for j in range(N+1)]
matrix[0] = [1,1,1,1,1,1]
for i in range(N+1):
    matrix[i][0] = 1
    for j in range(1,6):
        if i - penny[j] > 0:
            matrix[i][j] = sum(matrix[i- penny[j]][0:j+1])
        if (i == penny[j]) == 0:
            matrix[i][j] = 1
print(sum(matrix[i][:]))