import random

m = int(input("numarul maxim="))

rand_list = []
n = 10000
for i in range(n):
    rand_list.append(random.randint(0, m-1))
L2 = sorted(rand_list)


i = 1
while i < m:
    bins = [[] for i in range(10)]
    for nr in rand_list:
        n = (nr//i) % 10
        bins[n].append(nr)

    rand_list.clear()
    for k in range(0, len(bins)):
        for j in range(0, len(bins[k])):
            rand_list.append(bins[k][j])
    i*=10

i = 1
ok = 0

i = 0
ok = 1
while ok:
    ok = 0
    bins = [[] for _ in range(2**16)]
    for nr in rand_list:
        if (nr >> i) > 2**16-1:
            ok = 1
        n = (nr>>i)%(2**16)
        bins[n].append(nr)

    rand_list.clear()
    for k in range(0, len(bins)):
        for j in range(0, len(bins[k])):
            rand_list.append(bins[k][j])
    i+=16


i = 1
ok = 1
while ok:
    ok = 0
    bins = [[] for _ in range(1000)]
    for nr in rand_list:
        if (nr >> i) > 999:
            ok = 1
        n = (nr // i)%1000
        bins[n].append(nr)

    rand_list.clear()
    for k in range(0, len(bins)):
        for j in range(0, len(bins[k])):
            rand_list.append(bins[k][j])
    i*=1000

print(rand_list)
print(L2)
print(rand_list == L2)

def mergesort(List):
    if len(List) == 1:
        return List

    mid = len(List)//2
    L = List[:mid]
    R = List[mid:]

    return merge(mergesort(L), mergesort(R))

def merge(L, R):
    li = ri = 0
    List = []
    while len(L) > li and len(R) > ri:
        if L[li] < R[ri]:
            List.append(L[li])
            li+=1
        else:
            List.append(R[ri])
            ri+=1

    List = List + L[li:] + R[ri:]
    return List



newList = mergesort(rand_list)
print(newList == L2)

def quickSort(List, left, right):
    if left<right:
        index = part(List, left, right)

        quickSort(List, index+1, right)
        quickSort(List, left, index-1)
    return List

def part(List, left, right):
    pivot = List[right]
    j = left
    for i in range(left, right):
        if List[i] <= pivot:
            swap(List, j, i)
            j+=1
    swap(List, j, right)
    return j

def swap(List, i, j):
    aux = List[i]
    List[i] = List[j]
    List[j] = aux

print(quickSort(rand_list, 0, len(rand_list)-1) == L2)