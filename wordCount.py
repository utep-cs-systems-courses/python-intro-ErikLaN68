#! /usr/bin/env python3

#Takes the file to be read as first parameter and file to save to
import os
from sys import argv, stderr, exit

if(len(argv) != 3):
    print("Error")
    exit()

inputFile = open(argv[1], "r")
inputString = inputFile.readlines()
print(len(inputString))

wordDict = dict()
for line in inputString:
    tokens = line.split(" ")
    for word in tokens:
        if not word.isalnum():
            word = word.replace(".","").replace(",","").replace("\n","")
            if word in wordDict:
                count = wordDict.get(word)
                count = count + 1
                wordDict.update({word: count})
            else:
                wordDict.update({word: 1})
        elif word in wordDict:
            count = wordDict.get(word)
            count = count + 1
            wordDict.update({word: count})
        else:
            wordDict.update({word: 1})
            

outputFile = open(argv[2], "w")
for key, value in wordDict.items():
    outputFile.write(key + " " + str(value) + "\n")