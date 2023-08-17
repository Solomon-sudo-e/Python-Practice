# Collections : Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaaabbbbbbbbcccc"
my_counter = Counter(a)
# print(my_counter)
#Shows all the unique keys and how many times they are showed.
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements())) #Allows it to be used as all different elements.

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(12,3)
print(pt.x, pt.y)

from collections import OrderedDict
#Just like a regular dictionary that remembers the items order when inserted
#Mainly just important for older python versions

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int) #Returns dictionary with the type selected.
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
print(d)

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)
d.popleft()
print(d)
#d.clear()
d.extendleft([4, 5, 6, 7, 8])
print(d)
d.rotate(1) #Rotates elements to the right one.
print(d)
