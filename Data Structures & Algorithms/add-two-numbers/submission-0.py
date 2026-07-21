# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=''
        num2=''
        my_sum=''
        

        while l1:
            num1+=str(l1.val)
            l1=l1.next
        
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        

        print(num2)
        print(num1)
        my_sum=int(num1[::-1])+int(num2[::-1])
        print(my_sum)

        my_sum=str(my_sum)

        my_sum=my_sum[::-1]
        print(my_sum)

        dummy_node=ListNode()
        my_list=dummy_node

        for char in range(len(my_sum)):

            new_node=ListNode(int(my_sum[char]))
            
            my_list.next=new_node

            my_list=my_list.next
        

        return dummy_node.next

