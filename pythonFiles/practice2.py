i = 0
numbers = []

while i<6:
    print "at the top i is %d" % i
    numbers.append(i)

    i+=1
    print "Numbers now: " % numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

items = range(0,6)
items.reverse()
for index, item in enumerate(items):
    print index,item
