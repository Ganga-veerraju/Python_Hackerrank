from collections import Counter
input()
rooms = input().split()
c = Counter(rooms)
print(c.most_common()[-1][0])
