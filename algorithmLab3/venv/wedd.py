couple_of_people = dict()
visited = []
List_of_Clans=[]
result=[]
number_of_possible_pairs=0

def addDictList(values):
    couple_of_people.setdefault(int(values[0]),[])
    if int(values[0]) in couple_of_people.keys():
        couple_of_people[int(values[0])].append(int(values[1]))
    else:
        couple_of_people[int(values[0])] = int(values[1])

def orientedGraph():
    couple_of_people_copy=couple_of_people.copy()
    for i in couple_of_people.values():
        for j in i:
            couple_of_people_copy.setdefault(j,[])
    for i in couple_of_people_copy.keys():
        for j in couple_of_people.keys():
            if i in couple_of_people_copy[j]:
                couple_of_people_copy.setdefault(i,[])
                couple_of_people_copy[i].append(j)
    return couple_of_people_copy

def clan():
    dfs(copyList,min(copyList.keys()))
    visited_copy=visited.copy()
    List_of_Clans.append(visited_copy)
    for d in visited :
        del copyList[d]
    visited.clear()
    if len(copyList.keys()) == 0 :
        return List_of_Clans
    else:
        clan()

def dfs(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)

with open ('Text') as Text:
    for line in Text:
        values = line.split(",")
        addDictList(values)

copyList = orientedGraph().copy()

clan()

List_of_Clans_Copy = List_of_Clans.copy()
List_of_Clans_Copy.pop(0)
List_of_Clans.pop(len(List_of_Clans)-1)
for h in List_of_Clans:
    for p in List_of_Clans_Copy:
        for i in h:
            for j in p:
                if (i+j)%2==1:
                    result.append(str(i)+"/"+str(j))
                    number_of_possible_pairs+=1

print(number_of_possible_pairs,result)





