# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:55:31 2018

@author: Lenovo
"""
# =============================================================================
# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。
# =============================================================================
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #处理特殊情况
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        #用两个辅助变量记录原始两个链表的除去排序部分的首节点
        node1 = pHead1
        node2 = pHead2
        #用一个辅助变量head记录merger之后的链表的头结点
        head = ListNode('a')
        #辅助变量last，表示merger之后链表的最后一个节点，便于和剩下的链表相连
        last = head
        while node1 != None and node2 != None:
            #当第一个链表的节点值小于第二个链表的节点值时候，值小的节点连到last后面，并且该
            #链表窗口向后滑1格
            if node1.val <= node2.val:
                last.next = node1
                last = node1
                node1 = node1.next
            else:
                last.next = node2
                last = node2
                node2 = node2.next
        #最后因为node1或者node2为空的时候，意味着这一个链表已经排序完成，另外一个链表没排好的部分
        #直接连到last上
        if node1 ==  None:
            last.next = node2
        elif node2 == None:
            last.next = node1
        return head.next

if __name__ == "__main__":
    solution = Solution()
    node_7 = ListNode(17)
    node_6 = ListNode(13)
    node_5 = ListNode(11)
    node_4 = ListNode(7)
    node_3 = ListNode(5)
    node_2 = ListNode(3)
    node_1 = ListNode(2)

    phead1 = node_1 
    phead2 = node_2
    phead1.next = node_3
    node_2.next = node_4
    node_3.next = node_5
    node_4.next = node_6
    node_5.next = node_7
    
    result = solution.Merge(phead1,phead2)
    while result != None:
        print(result.val)
        result = result.next