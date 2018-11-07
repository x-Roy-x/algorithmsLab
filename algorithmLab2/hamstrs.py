basic_data = []
list_hamsters = []
list_sum = []
with open ('Text.txt') as Text:
    for line in Text:
        values = line.split(",")
        if len(values) == 1:
            basic_data.append(int(values[0][0:]))
        elif len(values) == 2:
            list_hamsters.append([int(values[0]),int(values[1][:-1])])

def choice(basic_data,list_hamsters,list_sum):
    c = 0
    i=len(list_hamsters)-1
    b=len(list_hamsters)
    while i>=0 :
        a=list_hamsters[i][0] + list_hamsters[i][1]*(b-1)
        list_sum.append(a)
        c +=a
        i-=1
    list_sum.reverse()
    index = 0
    i=0
    max=list_sum[0]
    while i < len(list_sum) :
        if max <  list_sum[i]:
            max = list_sum[i]
            index = list_sum.index(max)
        i+=1
    if c>basic_data[0]:
        list_hamsters.pop(index)
        list_sum = []
        choice(basic_data,list_hamsters,list_sum)
    else :
        print(b)
        print(c)

print(basic_data)
print(list_hamsters)
choice(basic_data,list_hamsters,list_sum)

