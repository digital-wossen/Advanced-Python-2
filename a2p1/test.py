import student

from collections import deque
s = deque(["Eric", "John", "Michael"])
s.append("Terry")           # Terry arrives
s.append("Graham")          # Graham arrives
print(s.popleft())                 # The first to arrive now leaves
print(s.popleft())                 # The second to arrive now leaves
print(s)
d = ass
print(d)