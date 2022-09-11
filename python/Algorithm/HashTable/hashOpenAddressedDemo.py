from hashOpenAddressed import *

h = HashOpenAddressed(11)
h.insert(10)
h.insert(21)
h.delete(20)
h.insert(20)
h.insert(5)
h.insert(80)
h.insert(32)
h.insert(20)
h.insert(44)

item = 21
slot = h.search(item)
if slot == None:
    print("Search Failed for", item)
else:
    print("Search for", item, "Successful at slot", slot)