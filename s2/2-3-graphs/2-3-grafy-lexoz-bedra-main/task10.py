class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add(self, u, v, w):
        self.graph.append([u, v, w])

    def output(self, lst, root):
        out = []
        for i in range(self.v):
            if lst[i] != float("inf"):
                if i == root:
                    out.append('0')
                elif lst[i] == 0:
                    out.append("-")
                else:
                    out.append(str(lst[i]))
            else:
                out.append("*")
        return out

    def BellmanFord(self, root):
        lst = [float("inf")] * self.v
        lst[root] = 0
        for i in range(self.v - 1):
            for u, v, w in self.graph:
                if lst[u - 1] != float("inf") and lst[u - 1] + w < lst[v - 1]:
                    lst[v - 1] = lst[u - 1] + w

        for u, v, w in self.graph:
            if lst[u - 1] != float("inf") and lst[u - 1] + w < lst[v - 1]:
                lst[u - 1] = 0
                lst[v - 1] = 0

        return self.output(lst, root)


if __name__ == "__main__":
    with open("input.txt") as f:
        inn = f.readlines()
        n, m = map(int, inn[0].split())

    gr = Graph(n)
    root = int(inn[-1]) - 1
    for i in range(1, m + 1):
        u, v, w = map(int, inn[i].split())
        gr.add(u, v, w)

    with open('output.txt', 'w+') as g:
        g.write('\n'.join([str(i) for i in gr.BellmanFord(root)]))