# Reverse a linked list in place

# Given a linked list, with head and next attributes, reverse it.

# ex:
# nums = LList([1,2,3])
# rev_llist(nums)
# nums
# > [3,2,1]

def rev_llist(l):
    curr = l.head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    l.head = prev
    return l
