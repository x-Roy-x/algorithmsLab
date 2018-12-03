def binaryNumber(number):
    result=0
    lenght=len(number)
    for i in range(lenght):
        result+=int(number[i])*(2**(lenght-i-1))
    return result

def searchForDegree(number,numberInPower):
    for i in range(int(numberInPower)):
        power=number**i
        if power >= numberInPower:
            return i

def numberBinary(x):
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    return n

import itertools
binaryTape=""
combinationsOptions=[]
possibleNumbers=[]

for line in open("Text"):
    values= line.split(",")
binary=values[0]
value=int(values[1][0:])

for i in range(searchForDegree(value,binaryNumber(binary))+1):
    n=numberBinary(value**i)
    possibleNumbers.append(int(n))

for p in itertools.product(possibleNumbers, repeat=3):
    binaryTape=str(p[0])+str(p[1])+str(p[2])
    if binaryTape == binary :
        combinationsOptions.append(p)
    a=""

print(possibleNumbers)
print(binary,value)
print(combinationsOptions)

