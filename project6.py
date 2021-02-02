# Program opens up names.txt file - reads the names into a list, cleans up
# the names in the list to remove any trailing newlines, then counts number of 
# names that have less than 4 characters
###############################################################################


'''
basically we have to print out a count of how many words from the names.txt file include at least one of the letters from my seven letter word
so to start off what are the letters in my seven letter word: F,E,R,R,A,R,I
how many words are in the txt file: 5163
question is out of those 5163 words, how many have at least one of the following letters: F,E,R,R,A,R, or I
'''



def readNames(fileName):
	'''
	Function reads names from a file into a list and returns it
	'''

	# first we create an empty List called namesList
	namesList = [] 

	# then we open up a file called fileName 
	# and read all the lines into namesList
	with open(fileName,'rt') as namesFile:
		namesList = namesFile.readlines()

	# in some environments (Mac or Windows),
	# the names read from the file might have a trailing space or newline
	# what we will do now is to read each name from namesList
	# and clean up each name (remove trailing space and newlines)
	# and put it in a new list called returnList

	returnList = [] # let's start with an empty list

	
	for name in namesList:
		if name.endswith('\n'):     # look up endswith() method
			name = name.rstrip()    # look up rstrip() method
			returnList.append(name) # add to final list

	return returnList

def countNames(listOfNames):
	'''
	Given a list of names, this counts the number of names that has a length less than 100
	'''

	count = 0
	for name in listOfNames:
		if len(name) < 100:
			count += 1

	return count

myFirstLetter = "F"
mySecondLetter = "E"
myThirdLetter = "R"
myFourthLetter = "R"
myFifthLetter = "A"
mySixthLetter = "R"
mySeventhLetter = "I"

namesList = readNames('/Users/SahilRajapkar/Desktop/names.txt')
count = countNames(namesList)

count100=0
words = namesList
for word in words:
    if myFirstLetter == "F" in words or \
       mySecondLetter == "E" in words or \
       myThirdLetter == "R" in words or \
       myFourthLetter == "R" in words or \
       myFifthLetter == "A" in words or \
       mySixthLetter == "R" in words or\
       mySeventhLetter == "I" in word:
        count100+=1


        
print(count100)
