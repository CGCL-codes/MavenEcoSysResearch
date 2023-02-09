# @author: Alan
# @Date: 2022/6/20 
# @Time: 上午11:40
# @Email: 2785941910@qq.com
# @File: use_networkx.py


import networkx
import sys
from interruptingcow import timeout

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

    # try:
    #     with timeout(30, exception=RuntimeError):
    #         paths = [i for i in networkx.all_simple_paths(G, start, end)]
    # except RuntimeError:
    #     print("TIME OUT")
    paths = [i for i in networkx.all_simple_paths(G, start, end)]
    for index, path in enumerate(paths):
        for i in path:
            print(i, end="")
            print(" ", end="")
        if index != len(paths) -1 :
            print("\n")


if __name__ == "__main__":
    get_path(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))