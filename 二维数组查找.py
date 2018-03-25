# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:15:53 2018

@author: Lenovo
"""
#排序好的一维数据使用二分查找
def find_one_dimension(start,end,target,array):
	mid = (start + end)//2
	if (mid == start )|(mid == end):
		return False,mid
	if array[mid] == target:
		return True,mid
	elif array[mid] > target:
		return find_one_dimension(start, mid, target, array)
	elif array[mid] < target:
		return find_one_dimension(mid, end, target, array)

#排序好的二维数据使用二分查找
def find_two_dimension(target, array):
	#生成对角线元素数据
	if array.shape == (0,1):
		if array == target:
			return True
		else:
			return False
	diag = [array[i, i]  for i in range(min(array.shape))]
	diag_result = find_one_dimension(0, len(diag) - 1, target, diag)
	if not diag_result[0]:
		tmp_array = np.array(array)
		print('tmp_array:',tmp_array)

		if find_two_dimension(target, array[diag_result[1]+1:, :diag_result[1]+1]):
			return True
		elif find_two_dimension(target,tmp_array[:diag_result[1]-1, diag_result[1]-1]):
			return True
		else:
			return False
		if left_result | right_result:
			return True
	else:
		return True

#排序好的二维数据使用二分查找
def find_two_dimension(x, y, length, height, target, array):
	#生成对角线元素数据
	if array.shape == (0,1):
		if array == target:
			return True
		else:
			return False
	array[x:x+height,y:y+length].shape
	diag = [array[i, i]  for i in range(min(length, height))]
	diag_result = find_one_dimension(0, len(diag) - 1, target, diag)
	if not diag_result[0]:
		if find_two_dimension(diag_result[1] + 1,target, array):
			return True
		elif find_two_dimension(target, array):
			return True
		else:
			return False
		if left_result | right_result:
			return True
	else:
		return True
def Find(target, array):
	# write code here
	x = len(array) - 1
	y = 0
	while x >= 0 | y <= len(array[1]):
		if array[x][y] == target:
			return True
		elif array[x][ y] > target:
			x = x - 1
		elif array[x][y] < target:
			y = y + 1 
	return False
