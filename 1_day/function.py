def function (input):
    file = input
    first = 0
    second = 0
    totalSum = 0
    charInt = 0
    for line in file:
        #find first value
        for char in line:
            charInt = ord(char)-48
            if charInt > 0 and charInt <= 9:
                first = charInt
            if first != 0: 
                break 
            
        #find second value 
        for char in reversed(line):
            #sets a variable for the char's value and then offsets, as ord'ed ints from a string need an offset FUCK ORD
            charInt = ord(char)-48
            if charInt > 0 and charInt <= 9:
                second = charInt
            if second != 0:
                break 

        #keep running total and reset the first and second values for to not trigger and early break 
        totalSum += ((first * 10)+ second)
        first = 0
        second = first
    return totalSum
