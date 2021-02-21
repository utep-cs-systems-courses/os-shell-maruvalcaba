#! /usr/bin/env python3
# Manuel Ruvalcaba
# Theory of Operating Systems
# Shell lab
# This lab is a mini-shell that is supposed to mimic bash shell

import os, sys, time, re 
from myread import myReadLines
from redirect import hasRedirect, validateRedirect
import pipes
pid = os.getpid()

def main():
    while(1):
        if 'PS1' in os.environ and len(os.environ['PS1']) < 3:
            os.write(1, (os.environ['PS1']).encode())
        else:
            os.write(1,"$ ".encode())
        argsString = myReadLines()
        if argsString == "":
            sys.exit(0)
        args = argsString.split() # get user input and tokenize in one line
        if(args == []):                # if there was no input, continue to the next loop
            continue
        elif args[0] == "exit":        # if command is 'exit', the shell will close
            sys.exit(1)
        elif args[0] == "cd":          # changes current directory
            if(len(args) == 1):
                os.chdir("..")
            else:
                os.chdir(args[1])
            continue;
        rc = os.fork()                 # forks a child

        backGround = False;

        if('&' in args):
            backGround = True;
            args.remove('&')
        
        if rc < 0:                     # if rc is negative, fork failed
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)
        
        elif rc == 0: # if rc == 0, it is the child
            if(pipes.hasPipes(args)):
                if(pipes.validPipes(args)):
                    doPipes(args)
                else:
                    os.write(2, ("Invalid Pipe formatting. \n").encode())
                    sys.exit(1)
            if(hasRedirect(args)):  
                valid, inputRed, outputRed, args = validateRedirect(args) # validates the redirects
                if(valid == False):
                    os.write(2, ("Invalid Redirect formatting. \n").encode())
                    sys.exit(1)
                if(inputRed is not ""):                                  # if no input Redirect
                    os.close(0)
                    os.open(inputRed, os.O_RDONLY)
                    os.set_inheritable(0, True)
                if(outputRed is not ""):                                 # if no output Redirect
                    os.close(1)
                    os.open(outputRed, os.O_CREAT | os.O_WRONLY)
                    os.set_inheritable(1,True)
            try:
                os.execve(args[0], args, os.environ)
            except FileNotFoundError:
                pass
            for dir in re.split(":", os.environ['PATH']): # try each directory in the path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly
            
            os.write(2, ("%s: Command not found \n" % args[0]).encode())
            sys.exit(1)                 # terminate with error
            
        else:                           # parent (forked ok)
            if not backGround:
                childPidCode = os.wait()    # waits for child process to finish

            
def doPipes(args):
    leftArg, rightArg = pipes.splitCommand(args)
    pr,pw = os.pipe()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" %rc).encode())
        sys.exit(1)
    elif rc == 0:
        os.close(1)
        os.dup(pw)
        os.set_inheritable(1, True)
        for fd in (pr, pw):
            os.close(fd)
        if(hasRedirect(leftArg)):  
            valid, inputRed, outputRed, leftArg = validateRedirect(leftArg) # validates the redirects
            if(valid == False):
                os.write(2, ("Invalid Redirect formatting. \n").encode())
                sys.exit(1)
            if(inputRed is not ""):                                  # if no input Redirect
                os.close(0)
                os.open(inputRed, os.O_RDONLY)
                os.set_inheritable(0, True)
            if(outputRed is not ""):                                 # if no output Redirect
                os.close(1)
                os.open(outputRed, os.O_CREAT | os.O_WRONLY)
                os.set_inheritable(1,True)
        try:
            os.execve(args[0], args, os.environ)
        except FileNotFoundError:
            pass
        for dir in re.split(":", os.environ['PATH']): # try each directory in the path
            program = "%s/%s" % (dir, leftArg[0])
            try:
                os.execve(program, leftArg, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly
            
        os.write(2, ("%s: Command not found \n" % leftArg[0]).encode())
        sys.exit(1)                 # terminate with error
    else:
        os.close(0)
        os.dup(pr)
        os.set_inheritable(0,True)

        for fd in (pr,pw):
            os.close(fd)
        if pipes.hasPipes(rightArg):
            doPipes(rightArg)
            
        if(hasRedirect(rightArg)):  
            valid, inputRed, outputRed, rightArg = validateRedirect(rightArg) # validates the redirects
            if(valid == False):
                os.write(2, ("Invalid Redirect formatting. \n").encode())
                sys.exit(1)
            if(inputRed is not ""):                                  # if no input Redirect
                os.close(0)
                os.open(inputRed, os.O_RDONLY)
                os.set_inheritable(0, True)
            if(outputRed is not ""):                                 # if no output Redirect
                os.close(1)
                os.open(outputRed, os.O_CREAT | os.O_WRONLY)
                os.set_inheritable(1,True)
        try:
            os.execve(args[0], args, os.environ)
        except FileNotFoundError:
            pass
        for dir in re.split(":", os.environ['PATH']): # try each directory in the path
            program = "%s/%s" % (dir, rightArg[0])
            try:
                os.execve(program, rightArg, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly
            
        os.write(2, ("%s: Command not found \n" % rightArg[0]).encode())
        sys.exit(1)                 # terminate with error

        
if __name__ == "__main__":
    main()
