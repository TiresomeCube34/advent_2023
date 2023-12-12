from function import function 
from bigReplace import bigReplace

arrayLine = {}
index = 0
#open original input file
file = open('input.txt', 'r')
for line in file:
    #append word representations of #'s with their interger counterparts:
    #store in an array
    line = bigReplace(line)
    arrayLine[index] = line
    index += 1

file2 = open('appended_input.txt', 'w')
for i in arrayLine:
    file2.write(arrayLine[i])

##idk if i need to close and reopen as a readable, but just in case 
file2.close()
file2 = open('appended_input.txt', 'r')
result = function(file2)
print(result)
