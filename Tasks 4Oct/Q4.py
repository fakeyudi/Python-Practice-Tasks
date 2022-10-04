# str = "my name is SDET D M"
#       1)i need to get the frequency of every character in the string eg: {a:3,m:3,e:1.....}
#       2)i need to get the frequency sorted in asc order of frequency count , if the count is same than on the basis of alphabetical order eg { d:1,e:1, n:2.......}

str = "my name is SDET D M"
d = {}
for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

sortedDict = {v[0]: v[1] for v in sorted(d.items(), key=lambda x: (x[1], x[0]))}
print(sortedDict)