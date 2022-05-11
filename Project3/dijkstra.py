import math


def relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w[u][v]:
        d_s[v] = d_s[u] + w[u][v]
        p_s[v] = u


def dijkstra(w, s):
    n = len(w)
    d_s = [0] * n
    p_s = [0] * n

'''initialize'''
    for i in range(n):
        d_s[i] = math.inf
        p_s[i] = None
    d_s[s] = 0

    not_ready = [i for i in range(n)]

    while len(not_ready) != 0:
        u = not_ready[0]
        for i in not_ready:
            if d_s[i] < d_s[u]:
                u = i
        not_ready.remove(u)

        for v in not_ready:
            if w[u][v] != 0:
                relax(u, v, w, d_s, p_s)
    return d_s, p_s


def print_dijkstra(d_s, p_s, s):
    print(f'START: s = {s + 1}\n')
    for i in range(len(d_s)):
        j = int(i)
        path = []
        while j is not None and j >= 0:
            path.append(j + 1)
            j = p_s[j]
        path.reverse()
        print(f'd({i + 1}) = {d_s[i]} => [{" - ".join(map(str, path))}]\n')