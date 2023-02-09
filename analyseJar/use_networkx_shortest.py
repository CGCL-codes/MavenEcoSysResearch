# @author: Alan
# @Date: 2022/6/20
# @Time: 上午11:40
# @Email: 2785941910@qq.com
# @File: use_networkx.py


import networkx
import sys


def get_path(callFile, start, end):
    f = open(callFile, "r")
    AdjMatrix = []
    edges = []
    for line in f.readlines():
        cols = line.strip().split(" ")
        AdjMatrix.append(cols)
    for index_row, row in enumerate(AdjMatrix):
        for index_col, col in enumerate(row):
            if int(col) == 1:
                edges.append((index_row, index_col))
    G = networkx.DiGraph()
    G.add_edges_from(edges)
    path = [i for i in networkx.shortest_path(G, start, end)]
    for index, node in enumerate(path):
        print(node, end="")
        print(" ", end="")


if __name__ == "__main__":
    get_path(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))