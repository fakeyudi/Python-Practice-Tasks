# Q. String str = “aabbcab”
# given
# 1. consecutive characters count will not be more than 2 ., eg : aaab is an invalid input
# 2. if they are consecutive characters i need one of them to get removed
# 3. if they are not consecutive recurring than keep as it is. : output -> abcab


def checkAndReturn(str):
    str = list(str)
    i = 0
    ctr = 1
    while i < len(str)-1:
        if str[i] == str[i+1]:
            ctr+=1
            if ctr > 2:
                return("Invalid input")
            str.pop(i)
            i -= 1
        else:
            ctr = 1
        i += 1
    return("".join(str))
    

str = "aabbccab"
print(checkAndReturn(str))
