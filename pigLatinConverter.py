# Quick and Easy Program to teach 6th Grade Coding Students

#Essential Skills
    #If Statements
    #Input
    #Split()
    #basic functions

def ifVowel(a: str):
    """
        a: a char or str 
        rtype: a boolean that is true if the letter is a vowel and false if not
    
    """
    return a.lower() in ["a", "e", "i", "o", "u"]


# First, get the user's sentece
print("What sentence would you like me to convert?")
userInput = input()

#Break the sentence into words and punctuation
userInput = userInput.split(" ")

#Clean user input so that punctuation is seperated
index = 0
while(index < len(userInput)):
    for i in range(len(userInput[index])):
        #if not alphabetical, the character needs to be taken out to its own line
        if not userInput[index][i].isalpha():
            #Make the old word itself but seperate everything after the punctuation mark
            userInput.insert((index+1), userInput[index][i])
            userInput[index] = userInput[index][0:i]
            index += 1
            break

    index += 1

#Change each word into Pig Latin
for i in range(len(userInput)):
    if userInput[i].isalpha():
        #Only want to 
        if ifVowel(userInput[i][0]):
            #If a word starts with a vowel add -way to end 
            userInput[i] = userInput[i] + "way"
        else:
            #Find where the last consonant of the beginning of the word is
            j = 0
            while (not ifVowel(userInput[i][j]) and j < len(userInput[i])):
                #Special case: y can start a pig latin word, but counts as a vowel inside the word
                if userInput[i][j].lower() == 'y' and j != 0:
                    break
                j += 1
            
            #Add special logic to keep 'u' with 'q' if need be
            if userInput[i][j].lower() == 'q':
                if j+1 <len(userInput[i]) and userInput[i][(j+1)] =='u':
                    #increase j because the next letter needs to be moved over too
                    j += 1
                else:
                    print("There appears to be an issue. In English, a 'q' should be followed by a 'u'.")

            userInput[i] = userInput[i][j:(len(userInput[i]))] + userInput[i][0:j] + 'ay'            
            
#Make the sentence proper in punctuation by adding spaces when necessary
for i in range(len(userInput)):
    if i == 0:
        print(userInput[i], end = "")
    elif userInput[i][0].isalpha():
        print(" "+userInput[i].lower(), end = "")
    elif userInput[i] == ".":
        print(userInput[i]+" ", end= "")
    else:
        print(userInput[i], end = "")

#Add a new line for formatting
print()


#Essential Questions:
    #Why do we use .lower() in line 15?
    #Why do we need the while loop at line 49?
    #Why does it make sense to place ifVowel in a function?  Would you make any more functions if you were writing this code?