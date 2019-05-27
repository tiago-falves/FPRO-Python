def discard_middle(s):
    string=""
    if len(s)>3:
        string=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    return string
