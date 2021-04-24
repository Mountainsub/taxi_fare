input_line = input()
a,b = input_line.split()
index = int(a)
subject = int(b)
value = []
for i in range(index):
    input_line = input()
    c, d, e, f = input_line.split()
    words = [c, d, e, f]
    g = []
    for j in words:
        g.append(int(j))
    dist = g[0]
    term = g[1]
    norm = g[2]
    up = g[3]
    while dist <= subject:
        dist += norm
        term += up
    value.append(term)
print(min(value),max(value))
