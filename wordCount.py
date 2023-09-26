#! /usr/bin/env python3

#Takes the file to be read as first parameter and file to save to
# Missing s and need to pull words that have - between them
import os
from sys import argv, stderr, exit

if(len(argv) != 3):
    print("Error")
    exit()

inputFile = open(argv[1], "r")
inputString = inputFile.readlines()
print("Number of lines in file " + str(len(inputString)))

def addToDict(word):
    if not word.isalpha():
        word = word.replace(".","").replace(",","").replace(";","").replace(":","")
        if word in wordDict and len(word) != 0:
            count = wordDict.get(word)
            count = count + 1
            wordDict.update({word: count})
        else:
            if len(word) != 0:
                wordDict.update({word: 1})
    elif word in wordDict and len(word) != 0:
        count = wordDict.get(word)
        count = count + 1
        wordDict.update({word: count})
    else:
        if len(word) != 0:
            wordDict.update({word: 1})

wordDict = dict()
for line in inputString:
    tokens = line.split(" ")
    for word in tokens:
        word = word.lower().strip()
        if "-" in word:
            tempWord = word.split("-")
            for w in tempWord:
                addToDict(w)
        elif "'" in word:
            tempWord = word.split("'")
            for w in tempWord:
                addToDict(w)
        else:
            addToDict(word)
            
print("Words in Dict " + str(len(wordDict)))
keyList = list(wordDict.keys())
keyList.sort()

outputFile = open(argv[2], "w")

for key in keyList:
    outputFile.write(key + " " + str(wordDict.get(key)) + "\n")
    
print(wordDict.get("s"))