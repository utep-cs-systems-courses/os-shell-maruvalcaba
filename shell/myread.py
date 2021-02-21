#! /usr/bin/env python3
# Manuel Ruvalcaba
# Theory of Operating Systems
# Shell lab
# This lab is a mini-shell that is supposed to mimic bash shell

import os, sys, time, re

next = 0              # next character
limit = 0             # limit of buffer
sbuf = ""             # string buffer
ibuf = ""             # input buffer

def getChar():
    global sbuf
    global next
    global limit                        # variables needed for reading
    global ibuf
    if(next == limit):                  # if we are done reading 
        next = 0;
        ibuf = os.read(0, 100)             # reads the next 100 bytes
        sbuf = ibuf.decode()
        limit = len(sbuf)               # limit is the amount of characters
        if(limit == 0):                 # if there was nothing left to read
            return ''
    c = sbuf[next]                      # returning the next character
    next += 1
    return c

def myReadLines():
    x = getChar()                       # gets character
    line = ""
    if(x == ''):
        return line
    while(x != '\n'):                   # while next character is not a new line
        line += x
        x = getChar()                   # keeps on adding lines
    line += '\n'
    return line
