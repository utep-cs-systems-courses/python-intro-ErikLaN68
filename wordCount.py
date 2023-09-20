#! /usr/bin/env python3

import os
from sys import argv, stderr, exit

if(len(argv) != 3):
    print("Error")
    exit()

inputFile = open(argv[1], "r")
inputString = inputFile.readlines()
print(len(inputString))

wordDict = dict()
for str in inputString:
    tokens = str.split(" ")
    for word in tokens:
        if not word.isalnum():
            for char in word:
                if char.isalnum() == False:
                    print(char)
                    word.replace(char," ")
        if word in wordDict:
            count = wordDict.get(word)
            count = count + 1
            wordDict.update({word: count})
        else:
            wordDict.update({word: 1})
            
print(wordDict.get("WHEN"))