# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:58:33 2018

@author: Lenovo
"""
# =============================================================================
# 输入一个链表，反转链表后，输出链表的所有元素。
# 注意是反转链表，并返回反转后的链表的首节点，而不仅仅是返回输出的值
# =============================================================================
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #如果输入节点为空，返回空
        if pHead == None:
            return None
        #如果输入的链表只有一个节点，返回这个节点
        if pHead.next == None:
            return pHead
        #当链表的节点个数>=2的时候进入到下面的循环中
        node = pHead
        last = None
        while node.next != None:
            #把当前节点的对下一个节点的引用保存下来
            tmp = node.next
            #当前节点的引用指向上一个节点
            node.next = last
            #在下一轮之前，把当前节点复制给last
            last = node
            #进入下一个节点
            node = tmp
        #当node等于倒数第二个节点的时候，node.next 就是最后一个节点，此时进入不了
        #循环，所以把最后一个节点的引用赋值给倒数第二个节点
        node.next = last
        return node

if __name__ == "__main__":
    node_6 = ListNode(13)
    node_5 = ListNode(11)
    node_4 = ListNode(7)
    node_3 = ListNode(5)
    node_2 = ListNode(3)
    head = ListNode(2)
    
    head.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    
    solution = Solution()
    result = solution.ReverseList(head)
    print(result.val)
#    print(result.next)
   