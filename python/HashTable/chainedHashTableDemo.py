from chainedHashTable import *
import sys
sys.path.append("../list")
from ..list.circularLinkedList import *
from ..list.listNode import *

h = ChainedHashTable(7)
h.insert(10)
h.insert(21)
h.delete(20)
h.insert(20)
h.insert(5)
h.insert(12)
h.insert(19)
h.insert(80)