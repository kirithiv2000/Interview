
#Array Questions

    #1.WAP to find the missing number in a given integer array of 1 to 100.
def missingNumberBetween_1_and_100(array):                  #declaration of function
	return [no for no in range(1,101) if  no not in array]  #number which are missing in the array is appended and returned
print(missingNumberBetween_1_and_100([1,2,3]))              #Calling of function

    #2.WAP to find the duplicate number on a given integer array.
def duplicateNumber(numberArray):                       #def is a keyword 
    List=[]                                             #declare a variable 
    repeatedList=[]                                     #declare a variable
    for number in numberArray:                          #iterate over given argument
        if number in List:                              #check the number is in List
            repeatedList.append(number)                 #appending the numbers which are duplicate
        else:                                           #if number not in list
            List.append(number)                         #appending the numbers which are not repeated
                                                        #if  no repeated numbers in the arg this runction return empty list
    return repeatedList                                 #return only the number which are repeated in a list

print(duplicateNumber([1,2,3,4,5,6,2]))                 #calling the function

    #3.WAP to find the largest and smallest number in an unsorted integer array.
def find_largest_and_smallest(unsortedArray):
    largestNumber =unsortedArray[0]
    smallestNumber=unsortedArray[0]
    for number in unsortedArray:
        if number>largestNumber:
            largestNumber=number
        if number<smallestNumber:
            smallestNumber=number
    return [largestNumber,smallestNumber]
find_largest_and_smallest([i for i in range(1,100)])

    #4.WAP to find all pairs of an integer array whose sum is equal to a given number.
def integerPairs(integerList,givenNumber):                                                                                  #declaring a function with two argument
    all_pairs_of_sum_equal_to_given_number=[]                                                                               #declaring a variable empty list
    for firstNumber in range(len(integerList)):                                                                             #iterating over a range of len of giver list
        for secondNumber in range(len(integerList)):                                                                        #iterating over a range of len of given list
            if firstNumber!=secondNumber:                                                                                   #ensure same numbers are not checked
                if integerList[firstNumber]+integerList[secondNumber]==givenNumber:                                         #checking the sum of two numbers 
                    if  [integerList[secondNumber],integerList[firstNumber]] not in all_pairs_of_sum_equal_to_given_number: #restricting the repeated pairs
                        all_pairs_of_sum_equal_to_given_number.append([integerList[firstNumber],integerList[secondNumber]]) #appending the pairs in a list
    return all_pairs_of_sum_equal_to_given_number                                                                           #returning all the pairs in a list
print(integerPairs([1,2,3,4,5,7],3))                                                                                        #calling the function

    #5.WAP to find duplicate numbers in an array if it contains multiple duplicates.
def haveMultipleDuplicates(array):                      #def is a keyword 
    List=[]                                             #declare a variable 
    repeatedList=[]                                     #declare a variable
    for number in array:                                #iterate over given argument
        if number in List:                              #check the number is in List
            repeatedList.append(number)                 #appending the numbers which are duplicate
        else:                                           #if number not in list
            List.append(number)                         #appending the numbers which are not repeated
                                                        #if  no repeated numbers in the arg this runction return empty list
    returnable =list(set(repeatedList))
    print(len(returnable))
    return returnable if len(returnable)>1  else []     #return only when the list have more than one repeated numbers

print(haveMultipleDuplicates([1,2,3,4,5,6,2,3]))        
    #6.WAP to remove duplicates from a given array in Java.

    #7.WAP to sort an integer array in place using the quicksort algorithm.
def pivots_position(list1,first,last):
 	pivot=list1[first]
 	left=first+1
 	right=last
 	while 1:
 		while left<=right and list1[left]<=pivot:                      #finding the position from right
 			left+=1
 		while right>=left and pivot<=list1[right]:                     #finding the position from left
 			right-=1
 		if left>right:                                                           
 			list1[first],list1[right]=list1[right],list1[first]
 			break
 		else:	
 			list1[left],list1[right]=list1[right],list1[left]
 	return right

def quick_sort(list1,first,last):
 	if first<last:
 		p=pivots_position(list1,first,last)
 		quick_sort(list1,p+1,last)
 		quick_sort(list1,first,p-1)
		
a=[4,3,2,1,5,6,7,7,7,7]
quick_sort(a,0,len(a)-1)
print(a)
    #8.WAP to remove duplicates from an array in place.
def removeDuplicates(array):                            #def is a keyword 
    indexList   =[]                                     #declare a variable 
    index       =0                                      #declare a variable 
    while 1:                                            #while True
        if index==len(array):                           #is loop need to stop (check)
            break                                       #break is a keyword to stop the iteration of loop
        count=array.count(array[index])                 #counting the number in the list
        if count==1:                                    #is present one time (check) in the list
            index+=1                                    #incriment 
        else:
            array.pop(index)                            #removing duplicates by using the index
removeDuplicates(a)                                     #calling the  function
print(a)             
    #9.WAP to reverse an array in place in Java.

    #10.WAP to  remove duplicates in an array without using any library.
def removeDuplicates(array):                            #def is a keyword 
    indexList   =[]                                     #declare a variable 
    index       =0                                      #declare a variable 
    while 1:                                            #while True
        if index==len(array):                           #is loop need to stop (check)
            break                                       #break is a keyword to stop the iteration of loop
        count=array.count(array[index])                 #counting the number in the list
        if count==1:                                    #is present one time (check) in the list
            index+=1                                    #incriment 
        else:
            array.pop(index)                            #removing duplicates by using the index
removeDuplicates(a)                                     #calling the  function
print(a)          

