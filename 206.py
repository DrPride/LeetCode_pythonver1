class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:  
            return head;  
        pre=None;  
        cur=head;  
        h=head; 
        #描述头节点的状态，然后去确认现节点的状态
        while cur:  
            h=cur;  
            tmp=cur.next;  
            cur.next=pre;  
            pre=cur;  
            cur=tmp;  
        return h; 
