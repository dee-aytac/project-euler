#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode()
        current = answer
        sum_ = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l1 else 0
            sum_ += val1 + val2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        print(str(sum_)[::1])
        for char in str(sum_)[::1]:
            print(type(current))
            current.val = ListNode(int(char))
            current = current.next
        return answer.next


solution = Solution()
a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
print(solution.addTwoNumbers(a, b))