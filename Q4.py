def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s

print(superReducedString('aaabccddd'))