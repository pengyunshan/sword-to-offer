# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:00:48 2018

@author: Lenovo
"""


# =============================================================================
# 输入一个链表，输出该链表中倒数第k个结点。
# =============================================================================
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #下面这个解释有瑕疵，求导数第一个的时候，取不到，正确的做法是在while里面初始化first_node
    #和second_node,或者在首节点head前使用一个头节点
    def FindKthToTailII(self, head, k):
        # write code here
        #设置衣服辅助变量node，表示当前所在的链表的节点，node初始化为head
        first_node = head
        #一个辅助变量step，记录当前是第一个指针访问到正数第几个节点
        step = 1
        while first_node.next != None:
            step += 1
            first_node = first_node.next
    
            if step == k:
                second_node = head
            elif step > k:
                second_node = second_node.next
        if step < k:
            return "list out of index"
        else:
            return second_node
        
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        first_node = head
        #一个辅助变量step，记录当前是第一个指针访问到正数第几个节点
        step = 0
        while first_node.next != None:
            step += 1
            if step == 1:
                first_node = head
            else:
                first_node = first_node.next
                
            if step == k:
                second_node = head
            elif step > k:
                second_node = second_node.next
        if step < k:
            return None
        else:
            return second_node
    
    def FindKthToHead(self, head, k):
        # write code here
        #设置衣服辅助变量node，表示当前所在的链表的节点，node初始化为head
        node = head
        while k>1:
            node = node.next
            k-=1
        return node.val    
if __name__ == "__main__":
    #建立一个6个节点组成的链表
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
    result = solution.FindKthToTail(head,6)
    print(result)