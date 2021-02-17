


def hasRedirect(args):
    if "<" in args or ">" in args:
        return True
    return False

def validateRedirect(args):
    numInput = 0
    numOutput = 0
    normalArgs = [];
    inputArg = ""
    outputArg = ""
    i = 0
    while(i < len(args)):
        if(args[i] == ">" or args[i] == "<"):
            if(i+1 >= len(args)):
                return False, "", "", []
            if(args[i+1] == ">" or args[i+1] == "<"):
                return False, "", "", []
            if(args[i] == "<"):
                numInput += 1
                if numInput > 1:
                    return False, "", "", []
                inputArg = args[i+1]
                i+=1
            if(args[i] == ">"):
                numOutput += 1
                if numOutput > 1:
                    return False, "", "", []
                outputArg = args[i+1]
                i+=1
        else:
            normalArgs.append(args[i])
        i+=1
    return True, inputArg, outputArg, normalArgs
            
            
