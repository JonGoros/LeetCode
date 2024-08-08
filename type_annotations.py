from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def Array2ListNode(array: List):

    if len(array) == 0: return None

    listNode: Optional[ListNode] = None
    node: ListNode

    for i in array:

        if listNode == None:
            listNode = ListNode(i)
            node = listNode
        else:
            node.next = ListNode(i)
            node = node.next
    
    return listNode

def ListNode2Array(listNode: ListNode):

    if listNode == None: return []

    node = listNode

    array = []

    while node != None:

        array.append(node.val)
        node = node.next
    
    return array
