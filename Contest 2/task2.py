def brackets_check(s):
    brackets=[]
    pairs={')':'(',']':'[','}':'{'}
    for bracket in s:
        if bracket in ['(','{','[']:
            brackets.append(bracket)
        elif bracket in [')','}',']']:
            if brackets[-1]==pairs[bracket]:
                brackets.pop()
            else:
                return False
    if brackets:
        return False
    else:
        return True
brack=input()
if brackets_check(brack):
    print('Yes')
else:
    print('No')