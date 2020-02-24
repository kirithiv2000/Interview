class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.
        self.prev = None

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)
nodeF = Node(6)

nodeG=Node(9)
nodeF.next=nodeG
nodeG.prev=nodeF

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF

nodeF.prev = nodeE
nodeE.prev = nodeD
nodeD.prev = nodeC
nodeC.prev = nodeB
nodeB.prev = nodeA

#Linked List Questions
    #6.WAP to find the length of a singly linked list.
def lengthOfSinglyLinkedList(head): #Function with one argument
    count=1                         #Declare a variable count 
    while head.next:                #if head.next = None then the loop break
        count+=1                    #count=count+1
        head=head.next              #next node
    return count                    #return count


    #5.WAP to remove duplicate nodes in an unsorted linked list.
def removeDuplicate(head):           #Function declaration
    List=[]                          #Declare a variable List with an empty list
    nextHead=head.next               #next node
    while nextHead:                  #if nextHead!=None then the loop will run 
        if head.data in List:        #Check data is repeated 
            head.prev.next=head.next #removing the repeated data
            print(List)
        else:                        #data is not repeated
            List.append(head.data)   #appending data which are not repeated in the list 
        head=head.next
        nextHead=head.next
    if head.data in List:
        head.prev.next=head.next
        
print(lengthOfSinglyLinkedList(nodeA))
removeDuplicate(nodeA)
print(lengthOfSinglyLinkedList(nodeA))

def show(head):
    while head.next:                #if head.next = None then the loop break
        print(head.data,end="=>")
        head=head.next              #next node
    print(head.data)
    #3.WAP to reverse a linked list.
def reverse(head):
    listofnode=[]                   #Declare a variable count 
    while head.next:                #if head.next = None then the loop break
        listofnode.append(head.data)
        head=head.next              #next node
    listofnode.append(head.data)

    while head.prev:
        head=head.prev
    count=len(listofnode)-1
    while head.next:
        head.data=listofnode[count]
        head=head.next
        count-=1
    head.data=listofnode[0]
    # listofnode[0]=None
show(nodeA)
reverse(nodeA)
show(nodeA)    
    #4.WAP to reverse a singly linked list without recursion.

def reverseSinglyLinked(head):
    listofnode=[]                   #Declare a variable count 
    start=head
    while head.next:                #if head.next = None then the loop break
        listofnode.append(head.data)
        head=head.next              #next node
    listofnode.append(head.data)


    count=len(listofnode)-1
    head=start                      #set the head to the first node
    while head.next:
        head.data=listofnode[count]
        head=head.next
        count-=1
    head.data=listofnode[0]        # listofnode[0]=None

reverseSinglyLinked(nodeA)
show(nodeA)
    #7.WAP to find the third node from the end in a singly linked list.
def thirdNodeFromEnd(NODE):
    count=lengthOfSinglyLinkedList(NODE)
    count-=3
    for loop in range(count):
        NODE=NODE.next
    return NODE.data

print(thirdNodeFromEnd(nodeA))
    #1.WAP to find the middle element of a singly linked list in one pass.
def middleElement(NODE):
    count=lengthOfSinglyLinkedList(NODE)
    if count%2==0:
        count=lengthOfSinglyLinkedList(NODE)//2-1
        for loop in range(count):
            NODE=NODE.next
        return(NODE.data,NODE.next.data)
    else:
        count=lengthOfSinglyLinkedList(NODE)//2
        for loop in range(count):
            NODE=NODE.next
        return(NODE.data)

# show(nodeA)
print(middleElement(nodeA))
    #8.WAP to find the sum of two linked lists using Stack.
def sumOftwoLinkedlist(headOfFirstList,headOfSecondList):
    sum=0
    for number in range(lengthOfSinglyLinkedList(headOfFirstList)):
        sum+=headOfFirstList.data
        headOfFirstList=headOfFirstList.next
    for number in range(lengthOfSinglyLinkedList(headOfSecondList)):
        sum+=headOfSecondList.data
        headOfSecondList=headOfSecondList.next
    return sum

print(sumOftwoLinkedlist(nodeA,nodeA))
