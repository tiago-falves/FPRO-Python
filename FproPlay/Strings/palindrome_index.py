def palindrome_index(s):

    if s==s[-1::-1]:
        return -1
    for i in range(len(s)):
        string=s[:i]+s[i+1:]

        if string==string[-1::-1]:
            return i
    return -1
