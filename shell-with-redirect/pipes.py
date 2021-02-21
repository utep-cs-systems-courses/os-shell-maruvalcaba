def hasPipes(args):
    if '|' in args:
        return True
    return False

def splitCommand(args):
    leftArg = []
    rightArg = []
    for i in range(len(args)):
        if(args[i] == '|'):
            leftArg = args[:i]
            rightArg = args[i+1:]
            break;
    return leftArg, rightArg

def validPipes(args):
    leftArgPos = 0;
    rightArgPos = 0;
    if args[0] == '|' or args[-1] == '|':
        return False
    for i in range(len(args)):
        if(args[i] == '|'):
            if(args[i+1] == '|'):
                return False
            if(leftArgPos == 0):
                leftArgPos = i;
            rightArgPos = i;
    for i in range(len(args)):
        if(i < leftArgPos):
            if args[i] == '>':
                return False
        elif(i > rightArgPos):
            if args[i] == '<':
                return False
        else:
            if args[i] == '>' or args[i] == '<':
                return False
    return True
                
                
