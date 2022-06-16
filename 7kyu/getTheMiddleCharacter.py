def get_middle(s):
    lent = len(s)
    if lent % 2 == 0:
        return s[int(lent/2)-1]+s[int(lent/2)]
    else:
        return s[int((lent/2))]
