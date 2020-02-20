
#Array Questions
    #WAP to find the duplicate number on a given integer array.
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

print(duplicateNumber([1,2,3,4,5,6,2]))


    #WAP to find all pairs of an integer array whose sum is equal to a given number.
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