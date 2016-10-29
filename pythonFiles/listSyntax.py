for index, item in enumerate(L):
    print index, item

item = L[index]
seq = L[start:stop]
seq = L[start:stop:step]

length = len(L)
L.append(item)
L.extend(sequence)
L.insert(index, item)
L.reverse()

del L[i]
del L[i:j]
item = L.pop() # last item
item = L.pop(0) # first item
item = L.pop(index)
L.remove(item)

L.sort()
out = sorted(L)