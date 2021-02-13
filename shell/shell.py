#! /usr/bin/env python3

import os, sys, time, re
from os import read, write

pid = os.getpid()

def tokenize(string):
    a = string.split()
    return a
        
def getChar():
    global sbuf
    global next
    global limit
    global ibuf
    if(next == limit):
        next = 0;
        ibuf = read(0, 100)
        sbuf = ibuf.decode()
        limit = len(sbuf)
        if(limit == 0):
            return ''
    c = sbuf[next]
    next += 1
    return c

def myReadLines():
    x = getChar()
    line = ""
    while(x != '\n'):
        line += x
        x = getChar()
        if(x == ''):
            return ''
    line += '\n'
    return line

while(1):
    write(1, '$ '.encode())
    ibuf = read(0, 100)
    sbuf = ibuf.decode()
    next = 0
    limit = len(sbuf)    
    a = tokenize(myReadLines())
    if(a == []):
        continue
    elif a[0] == "exit":
        sys.exit(1)
    args = a
    rc = os.fork()
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
        
    elif rc == 0:                   # child
        for dir in re.split(":", os.environ['PATH']): # try each directory in the path
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly
            
        os.write(2, ("Child:    Could not exec %s\n" % args[0]).encode())
        sys.exit(1)                 # terminate with error
            
    else:                           # parent (forked ok)
        childPidCode = os.wait()

