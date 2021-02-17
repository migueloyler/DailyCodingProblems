def isBipartite(graph):
    set1 = set()
    set2 = set()
    explored = set()
    q = [0]
    cnt = 0
    set1.add(0)
    while q:
        if len(explored) == len(graph):
            break
        el = q.pop(0)
        
        #if el in set1 or el in set2:
        #    continue
        if el not in explored:
            for i in graph[el]:
                if cnt % 2 == 0:
                    set2.add(i)
                else:
                    set1.add(i)
                if i not in explored:
                    q.append(i)
        explored.add(el)
        cnt += 1
    if len(set1 & set2) > 0:
        return False
    return True

print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))