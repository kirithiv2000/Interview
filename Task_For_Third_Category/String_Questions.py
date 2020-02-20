#1.String Questions
    #1.WAP to print duplicate characters in a string.

def print_duplicate_charactersInString(str):   #def is a keyword to declare user defined function 
    que=""                                     #Declaring variable que with empty string
    printed=''                                 #Declaring variable printed      
    for character in str:                      #Iterating over string
        if character in que:                   #Check character is in que  
            if character not in printed:       #Making sure that same character are not printed repeatedly
                print(character)               #printing the characters which are repeated
                printed+=character             #printed=printed+character add the characters which was printed recently 
        else:                                  #character not in que
            que+=character                     #que = que + character

print_duplicate_charactersInString('kirithivvr') #calling the user defined function

    #2.WAP to check if two strings are anagrams of each other.
def anagram_finder(str1, str2):                 #declaration of function       
    list_str1 = list(str1)                      #conver the str in list
    list_str2 = list(str2)                      #conver the str in list
    if sorted(list_str1) == sorted(list_str2):  #check both list are equal   
        return True                             #if both are same then return true
    else:                                       #not same or not equal
        return False                            #then return False

print(anagram_finder('vihtirik','kirithiv'))    #calling the function

    #3.WAP to print the first non-repeated character in a string.
def firstNon_RepeatedCharacter(str):             #Name of user defined function is firstNon_RepeatedCharacter
    for character in range(len(str)):            #Iterating using for Loop   
        firstHalf=str[:character]                #part of string before character
        secondHalf=str[character+1:]             #part of string after character
        if str[character] not in firstHalf:      #check character is in firstHalf 
            if str[character] not in secondHalf: #check character is in secondHalf
                print(str[character])            #print the first non-repeated character
                return str[character]            #returning the first non-repeated character

firstNon_RepeatedCharacter('kirithiv')           #calling the function of name firstNon_RepeatedCharacter


    #4.WAP to reverse a given string using recursion.
def reverse_a_string(str):                      #declaration of function
    if len(str) == 0:                           #if the length of string is 0
        return (str)                            #return the string
    else:                                       #if lenght is not 0
        var=reverse_a_string(str[1:])           #function calls itself with string without first character
        return (var + str[0])                   #function concatenation

print(reverse_a_string('kirithiv'))             #calling the function


    #5.WAP to check if a string contains only digits.
def stringOnlyContainDigitsCheck(givenString):  #declaration of function
    digits='0123456789'                         #declaring a variable digits with all the digits
    for character in givenString:               #iterating over givenString
        if character in digits:                 #check weather character is int or a alphabet
            pass                                #passing to next line
        else:                                   #if it is an alphabet
            return False                        #return false
    return True                                 #if the for loop run succesfully then the function will return True



    #7.WAP to count the number of vowels and consonants in a given string.
def countVowelConsonants(str):
    vowels="aeiou"                               #declaring a variable named vowels with english vowels in it
    space=0                                      #declare a variable with value 0
    vowelsCount=0                                #declare a variable with value 0
    for character in str.lower():                #iterating over string after converting string into lower case
        if character in vowels:                  #check it is vowel 
            vowelsCount+=1                       #incriment for count
        if character == " ":                     #check it is space
            space+=1                             #incriment for space
    consonantsCount=len(str)-vowelsCount         #FROM the length if we seprate count of vowels and
    consonantsCount-=space                       #space in the string we will get the no of consonants
    return [vowelsCount,consonantsCount]         #return count of vowels and count of consonants in a list


print(countVowelConsonants('kirithiv'))          #calling the function




    #12.WAP to check if a given string is a palindrome.
def palindrome(user1):                           #declaration of function      
	return True if user1[::-1]==user1 else False #return true if palindrome else false with the help of slicing
print(palindrome('nine'))                        #calling the function
