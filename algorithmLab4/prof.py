import math

oneWay=[]
allWays=[]
converted_to_int = []
the_path_of_one_proof=[]
oneWay=[]

def comb():
    for i in range(theNumberOfProofs):
        for j in range(theNumberOfProofs):
            if allListProof[i][j] == 0:
                if j == theNumberOfProofs-1:
                    number=allListProof[i][0]

                # elif i == theNumberOfProofs-1:
                #     i=0
                else:
                    number=allListProof[i][j+1]
                the_path_of_one_proof.append(number)

def rev():
    allListProof[0], allListProof[theNumberOfProofs-1]=allListProof[theNumberOfProofs-1],allListProof[0]
    for i in range(theNumberOfProofs):
        allListProof[i][0], allListProof[i][theNumberOfProofs-1]=allListProof[i][theNumberOfProofs-1],allListProof[i][0]
    return allListProof

for line in open("Text"):
    values= line.split(",")

for v in values:
    converted_to_int.append(int(v))

theNumberOfProofs = int(math.sqrt(len(values)))
fact=math.factorial(theNumberOfProofs)

allListProof = [[0 for i in range(theNumberOfProofs)] for i in range(theNumberOfProofs)]
for i in range(theNumberOfProofs):
    for j in range(theNumberOfProofs):
        allListProof[i][j] = converted_to_int[i * theNumberOfProofs + j]

for i in range(fact):
    comb()
    rev()

for i in the_path_of_one_proof:
    if len(oneWay) < theNumberOfProofs:
        oneWay.append(i)
    else:
        h=oneWay.copy()
        allWays.append(h)
        oneWay.clear()

for i in allWays:
    difference=max(i)- min(i)
    oneWay.append(difference)
print(allListProof)
print(min(oneWay))
