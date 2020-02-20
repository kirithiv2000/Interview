#Linked List Questions
    #WAP to find the length of a singly linked list.
def lengthOfSinglyLinkedList(head): #Function with one argument
    count=1                         #Declare a variable count 
    while head.next:                #if head.next = None then the loop break
        count+=1                    #count=count+1
        head=head.next              #next node
    return count                    #return count

    #WAP to remove duplicate nodes in an unsorted linked list.
def removeDuplicate(head):           #Function declaration
    List=[]                          #Declare a variable List with an empty list
    nextHead=head.next               #next node
    while nextHead:                  #if nextHead!=None then the loop will run 
        if head.data in List:        #Check data is repeated 
            head.prev.next=head.next #removing the repeated data
        else:                        #data is not repeated
            List.append(head.data)   #appending data which are not repeated in the list 
