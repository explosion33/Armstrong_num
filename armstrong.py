def armstrong(input):
    length = len(str(input))
    numString = str(input)
    fCalc = 0

    for i in range(0,length):
        num = int(numString[i])
        end = num ** length
        fCalc += end

    if fCalc == input:
        return True
    else:
        return False


inp = input("")

if armstrong(int(inp)) == True:
    print(str(inp) + " is an Armstrong number")

else:
    print(str(inp) + " is not an Armstrong number") 