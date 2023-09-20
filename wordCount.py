#! /usr/bin/env python3

import os
from sys import argv, stderr, exit

if(len(argv) != 3):
    print("Error")
    exit()

inputFile = open(argv[1], "r")
inputString = inputFile.readlines()

wordDic = dict()
for str in inputString:
    tokens = str.split(" ")
    