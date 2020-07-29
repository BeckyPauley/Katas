def xo(s):
    string = s.lower()
    exes =string.count('x')
    ohs = string.count('o')
    if exes == ohs:
        return True
    else:
        return False


print(xo("ooxx")) #=> true
print(xo("xooxx")) #=> false
print(xo("ooxXm")) #=> true
print(xo("zpzpzpp")) #=> true // when no 'x' and 'o' is present should return true
print(xo("zzoo")) #=> false
print(xo("XxXxOoOo0Y")) #=> true