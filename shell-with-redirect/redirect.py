# Manuel Ruvalcaba
# Theory of Operating Systems
# Shell lab
# This lab is a mini-shell that is supposed to mimic bash shell

def hasRedirect(args):           # checks if there is a redirect
    if "<" in args or ">" in args:
        return True
    return False

def validateRedirect(args):      # validates the redirect
    numInput = 0                 # stores number or redirects, only one of each
    numOutput = 0
    normalArgs = [];             # stores other normal arguments
    inputArg = ""                # stores input redirect argument
    outputArg = ""               # stores output redirect argument
    i = 0
    while(i < len(args)):
        if(args[i] == ">" or args[i] == "<"):   # if symbol indicates there is a redirect
            if(i+1 >= len(args)):               # if there are no more args
                return False, "", "", []
            if(args[i+1] == ">" or args[i+1] == "<"):    # if there are multiple symbols in a row
                return False, "", "", []
            if(args[i] == "<"):                          # finally, if it is input Redirect
                numInput += 1
                if numInput > 1:                         # if there are more than one redirect
                    return False, "", "", []             
                inputArg = args[i+1]                     # otherwise, store the argument
                i+=1                                     # skip stored argument
            if(args[i] == ">"):                          # if it is output redirect
                numOutput += 1
                if numOutput > 1:                        # do the same as the input
                    return False, "", "", []
                outputArg = args[i+1]
                i+=1                      
        else:                                            # else it is a normal arg
            normalArgs.append(args[i])
        i+=1
    return True, inputArg, outputArg, normalArgs         # valid
            
            
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
