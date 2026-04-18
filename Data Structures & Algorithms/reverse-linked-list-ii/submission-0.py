class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        # Step 1: reach node before left
        pre_left = dummy
        for _ in range(left - 1):
            pre_left = pre_left.next

        # Step 2: reach right node
        right_node = pre_left
        for _ in range(right - left + 1):
            right_node = right_node.next

        left_node = pre_left.next
        post_right = right_node.next

        # Step 3: cut
        pre_left.next = None
        right_node.next = None

        # Step 4: reverse
        reversed_head = self.reverse(left_node)

        # Step 5: reconnect
        pre_left.next = reversed_head
        left_node.next = post_right

        return dummy.next

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev