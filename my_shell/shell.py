#! /usr/bin/env python3

import os, sys, time, re
from os import read, write

pid = os.getpid()
next = 0              # next character
limit = 0             # limit of buffer
sbuf = ""             # string buffer
ibuf = ""             # input buffer

def main():
    while(1):
        write(1, '$ '.encode())    
        args = tokenize(myReadLines()) # get user input and tokenize in one line
        if(args == []):                # if there was no input, continue to the next loop
            continue
        elif args[0] == "exit":        # if command is 'exit', the shell will close
            sys.exit(1)                     
        rc = os.fork()                 # forks a child
        if rc < 0:                     # if rc is negative, fork failed
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        
        elif rc == 0:                   # if rc == 0, it is the child
            for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly
            
            os.write(2, ("Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error
            
        else:                           # parent (forked ok)
            childPidCode = os.wait()    # waits for child process to finish


def tokenize(string):
    a = string.split()                  # splits the string into tokens
    return a
        
def getChar():
    global sbuf
    global next
    global limit                        # variables needed for reading
    global ibuf
    if(next == limit):                  # if we are done reading 
        next = 0;
        ibuf = read(0, 100)             # reads the next 100 bytes
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
    while(x != '\n'):                   # while next character is not a new line
        line += x
        x = getChar()                   # keeps on adding lines
        if(x == ''):                    # if there is nothing left to read
            return line
    line += '\n'
    return line

if __name__ == "__main__":
    main()
