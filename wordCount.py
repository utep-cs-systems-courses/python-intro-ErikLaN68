#! /usr/bin/env python3

import os
import re
from sys import argv, stderr, exit

#The decoding of the file gives you an array of chars and they have to be formed into a word
def getTokens(input):
    curWord = ""
    wordList = []
    for letter in input:
        if letter.isalpha():
            curWord = curWord + letter
        else:
            wordList.append(curWord)
            curWord = ""
    return wordList

#Checks that the program has 2 file inputs
if len(argv) != 3 :
    print("Have to enter ./wordCount.py followed by input.txt and output.txt")
    exit()
#Checks that input file exist
if not os.path.exists(argv[1]):
    print('Inpute file can not be found')
    exit()

#Reads the input file and pulls infomatoin from it
inputFile = os.open(argv[1], os.O_RDONLY)
inputString = os.read(inputFile,os.path.getsize(argv[1]))
#Decodes the information and sends it to be put back to words
inputString = inputString.decode()
wordList = getTokens(inputString)

#Makes dict and handles the adding of the words to the dict
wordDict = dict()
for word in wordList:
    word = word.lower().strip()
    if word in wordDict and len(word) != 0:
        wordDict.update({word: wordDict.get(word)+1})
    elif len(word) != 0:
        wordDict.update({word: 1})

#Gets a list of keys and sorts
keyList = list(wordDict.keys())
keyList.sort()

#Creates and makes the outpute file writable
outFile = os.open(argv[2], os.O_WRONLY | os.O_CREAT)

#Runs through the dict to get words and amounts
for key in keyList:
    writeStr = key + " " + str(wordDict.get(key)) + "\n"
    os.write(outFile,writeStr.encode())
    
print('Words in input file have counted and saved in ' + argv[2])