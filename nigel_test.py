import re

line = "I promise I'm bridgin' the gap"
line = line.replace('"','').replace(',','').replace('.','').replace('?','').replace('!','').replace('*','').replace('/','').replace('.','').replace('-','')

print(line)


if "in'" in line:
    print('yes')