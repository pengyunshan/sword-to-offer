from __future__	 import print_function,division
import numpy as np




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListFromTailToHead(listNode):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # write code here
    tmp_list = []
    if listNode is  None:
        return tmp_list
    while listNode.next is not None:
        tmp_list.append(listNode.val)
        listNode = listNode.next
    tmp_list.append(listNode.val)
    return tmp_list[::1]


if __name__ == "__main__":
	# target = Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
	# print(target)
	
	# array = [1,10,11,12,15,16,18,20,25,27,29]
	# result = find_one_dimension(0, len(array)-1, 10, array)
	# print(position)
	# x = np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
	# result = find_two_dimension(7, x)
	# print(result)
	result = Find(2, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
	print(result)
