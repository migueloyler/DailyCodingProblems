'''
Let's represent an integer in a linked list format by having each node
 represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
'''
def sum_linked_list(l1,l2,res):
    carryVal = 0
    result = []
    while l1.head != None and l2.head != None:
        s = (l1.head() + l2.head() + carryVal)
        currVal = s % 10
        carryVal = s // 10
        l1 = l1.next()
        l2 = l2.next()
        result.append(currVal)
    if l1.head() == None:
        while l2.head != None:
            s = (l2.head() + carryVal)
            currVal = s % 10
            carryVal = s // 10
            result.append(currVal)
            l2 = l2.next()
            result.append(currVal)
    if l2.head() == None:
        while l2.head != None:
            s = (l2.head() + carryVal)
            currVal = s % 10
            carryVal = s // 10
            result.append(currVal)
            l1 = l1.next()
            result.append(currVal)
    return result
