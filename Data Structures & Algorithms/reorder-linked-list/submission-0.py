class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find middle
        middle = self.middle_of_the_list(head)

        # 2. Split
        second = middle.next
        middle.next = None

        # 3. Reverse second half
        second = self.reverse_list(second)

        # 4. Merge
        first = head
        while first and second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2

    def middle_of_the_list(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev