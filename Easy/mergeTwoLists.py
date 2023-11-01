#merging two sorted linked lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        tempList = head
        
        while list1 and list2:
            if list1.val < list2.val:
                tempList.next = list1
                list1 = list1.next
            else:
                tempList.next = list2
                list2 = list2.next
            tempList = tempList.next
        if list1:
            tempList.next = list1
        if list2:
            tempList.next = list2
        return head.next

#test

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

run_program = Solution()
newList = run_program.mergeTwoLists(list1, list2)
while (newList):
    print(newList.val)
    newList = newList.next
