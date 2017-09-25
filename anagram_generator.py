def all_perms(elements):
    """create anagram"""
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp
        

word = "abc"

print (list(all_perms(word)))
