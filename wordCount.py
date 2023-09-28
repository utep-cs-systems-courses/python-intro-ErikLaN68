#! /usr/bin/env python3

#Takes the file to be read as first parameter and file to save to
# Missing s and need to pull words that have - between them
import os
import re
from sys import argv, stderr, exit

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

if(len(argv) != 3):
    print("Have to enter ./wordCount.py followed by input.txt and output.txt")
    exit()

# inputFile = open(argv[1], "r")
# inputString = inputFile.readlines()
inputFile = os.open(argv[1], os.O_RDONLY)
print(inputFile)
inputString = os.read(inputFile,os.path.getsize(argv[1]))
print("Number of lines in file " + str(len(inputString)))
print(inputString)
inputString = inputString.decode()
print("Number of lines in file " + str(len(inputString)))
print(inputString)
wordList = getTokens(inputString)
print(wordList[0])

wordDict = dict()
for line in wordList:
    line = line.lower().strip()
    #using the \W+ splits the input line on all punctuation and whitespace
    tokens = re.split('\s',line)
    for word in tokens:
        if word in wordDict and len(word) != 0:
            wordDict.update({word: wordDict.get(word)+1})
        elif len(word) != 0:
            wordDict.update({word: 1})

keyList = list(wordDict.keys())
keyList.sort()

outputFile = open(argv[2], "w")

for key in keyList:
    outputFile.write(key + " " + str(wordDict.get(key)) + "\n")