class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        array = list()
        while self is not None:
            #print(self.val)
            array.append(self.val)
            self = self.next
        print(array)    

class Solution(object):
    def deleteDuplicates(self, head):
        current = ListNode(None)
        clean_list = current
        
        while (head is not None):
            #print ("lists")
            head.printList()
            current.printList()
            if head.val != current.val:
                #print("Before: Head {headval}, Clean {clean}".format(headval = head.val, clean= clean_list.val))
                newNode = ListNode(head.val, None)
                current.next = newNode
                current = current.next
                #print("After: Head {headval}, Clean {clean}".format(headval = head.val, clean= clean_list.val))
                
            head = head.next

        return clean_list.next
        

head_1 = ListNode(1, ListNode(1, ListNode(2)))
head_2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))


run_program = Solution()
run_program.deleteDuplicates(head_1).printList()

