def ispalindrome(s):
    rev=''.join(reversed(s))
    if(s == rev):
        return True
    return False

s= "malayalam"
ans = ispalindrome(s)

if (ans):
    print("yes")
else:
    print("no")