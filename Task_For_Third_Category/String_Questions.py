#1.String Questions
    #WAP to print duplicate characters in a string.

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

    #WAP to print the first non-repeated character in a string.
def firstNon_RepeatedCharacter(str):             #Name of user defined function is firstNon_RepeatedCharacter
    for character in range(len(str)):            #Iterating using for Loop   
        firstHalf=str[:character]                #part of string before character
        secondHalf=str[character+1:]             #part of string after character
        if str[character] not in firstHalf:      #check character is in firstHalf 
            if str[character] not in secondHalf: #check character is in secondHalf
                print(str[character])            #print the first non-repeated character
                return str[character]            #returning the first non-repeated character

firstNon_RepeatedCharacter('kirithiv')           #calling the function of name firstNon_RepeatedCharacter