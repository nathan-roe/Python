def findParenth(s):
    sVal = list(s)
    for i in range(0, len(sVal)):
        if sVal[i] == ')':
            return False
        elif sVal[i] == '(':
            for j in range(i, len(sVal)):
                if sVal[j] == ')':
                    sVal[i] = '1'
                    sVal[j] = '1'
                    break
    count = 0
    print(sVal)
    for x in range(0, len(sVal)):
        if sVal[x] == ')' or sVal[x] == '(':
            count += 1
    if count > 1:
        return False
    else:
        return True
print(findParenth("()()(asdfasd)()asdf())asdf)))asdf)(((asdfasdf(((asdf()()asdfasdf()()(adsfasdfasdf"))
print(findParenth("()()(()())(())"))
