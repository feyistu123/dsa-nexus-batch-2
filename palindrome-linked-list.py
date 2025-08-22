# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        num = head
        while num:
            st.append(num.val)
            num = num.next
        num2 = head
        while num2:
            if num2.val != st.pop():
                return False
            num2 = num2.next
        return True
