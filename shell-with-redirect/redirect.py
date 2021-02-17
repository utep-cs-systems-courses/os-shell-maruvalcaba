# Manuel Ruvalcaba
# Theory of Operating Systems
# Shell lab
# This lab is a mini-shell that is supposed to mimic bash shell

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
            
            
"""        
def tokenize(tokens):
    args = []                  is this how you do multi-line comment? keeping for now
    inputRed = ""
    outputRed = ""
    i = 0
    while(i < len(tokens)):
        if(tokens[i][0] == '<'):
            if(len(tokens[i]) == 1):
                inputRed = tokens[i+1]
                i += 1
            else:
                inputRed = tokens[i][1:]
        elif(tokens[i][0] == '>'):
            if(len(tokens[i]) == 1):
                outputRed = tokens[i+1]
                i += 1
            else:
                outputRed = tokens[i][1:]
        else:
            args.append(tokens[i])
        i+=1
    return args,inputRed,outputRed
"""
