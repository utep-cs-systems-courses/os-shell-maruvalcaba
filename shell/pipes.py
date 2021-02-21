#! /usr/bin/env python3
# Manuel Ruvalcaba
# Theory of Operating Systems
# Shell lab
# This lab is a mini-shell that is supposed to mimic bash shell

def hasPipes(args):
    if '|' in args:
        return True
    return False

def splitCommand(args):               # Splits the commands at the pipe and returns it
    leftArg = []                      # These hold the left and right side
    rightArg = []
    for i in range(len(args)):        # Iterates through and finds the pipe symbol
        if(args[i] == '|'):
            leftArg = args[:i]
            rightArg = args[i+1:]
            break;
    return leftArg, rightArg

def validPipes(args):                 # Checks to see if the syntax of the pipes are valid
    leftArgPos = 0;                        # Hold the positions of the first and last pipe symbol
    rightArgPos = 0;
    if args[0] == '|' or args[-1] == '|':  # If there is a pipe symbol in the first or last arg
        return False
    for i in range(len(args)):             # this loop finds the positions of pipe symbols
        if(args[i] == '|'):
            if(args[i+1] == '|'):          # If there are 2 consecutive pipes
                return False
            if(leftArgPos == 0):
                leftArgPos = i;
            rightArgPos = i;
    for i in range(len(args)):             # checks if redirect syntax within pipes is valid
        if(i < leftArgPos):
            if args[i] == '>':             # cannot have output redirect in first sub command
                return False
        elif(i > rightArgPos):             # cannot have input redirect on last sub command
            if args[i] == '<':
                return False
        else:
            if args[i] == '>' or args[i] == '<':
                return False
    return True
                
                
