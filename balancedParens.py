'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def isBalanced(s):
    curOpen = []
    countsDict = {'(': 0, ')':0, '{':0, '}':0, '[':0, ']':0}
    openers = set(['{', '[', '('])
    closers = set([')','}',']'])

    inverse = {'[':']', '(':')','{':'}'}

    #get counts of each element
    for i in range(len(s)): 
        countsDict[s[i]] += 1

    #if the counts don't match then we already know they're not balanced
    for k,v in countsDict.items(): 
        if k == '(':
            if countsDict[k] != countsDict[')']:
                return False
        if k == '{':
            if countsDict[k] != countsDict['}']:
                return False
        if k == '[':
            if countsDict[k] != countsDict[']']:
                return False

    #use a stack, make sure that everytime we close one, we know that 
    # it must match the opener at the top of stack
    for i in range(len(s)): 
        if i == 0:
            curOpen.append(s[i])
            continue
        if s[i] in openers:
            curOpen.append(s[i])
        else:
            lastOpen = curOpen.pop()
            if s[i] != inverse[lastOpen]:
                return False

    return True

print(isBalanced('([])[]([])'))

print(isBalanced('([)]'))

print(isBalanced('((()'))