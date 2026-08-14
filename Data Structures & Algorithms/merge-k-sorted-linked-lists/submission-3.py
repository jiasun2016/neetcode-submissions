import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        # 1. 将所有非空链表的头节点压入最小堆
        # 使用 count 作为索引标记，防止 val 相同时直接比较 ListNode 结构
        count = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
        
        dummy = ListNode(-1)
        curr = dummy
        
        # 2. 依次弹出堆顶最小值，并将其 next 节点压入堆中
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
                
        return dummy.next