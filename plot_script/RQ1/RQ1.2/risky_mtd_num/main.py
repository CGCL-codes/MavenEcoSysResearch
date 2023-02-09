import collections

import matplotlib.pyplot as plt
import pickle

def draw_bar_plot_downstream_risky_mtd():
    """
    Draw the histogram for Risky Method(RM) num in all downstream, when there exist more than ten RM, we denote it as >10.
    :return:
    """

    with open("raw_data/downstream_risky_mtd", "rb") as f:
        downstream_risky_mtd = pickle.load(f)

    nums = []

    for dep_name, risky_mtd in downstream_risky_mtd.items():
        if len(risky_mtd) == 0:                                         #Skip all the downstream that can not access the vulnerability
            continue
        if len(risky_mtd) > 10:
            nums.append(11)
        else:
            nums.append(len(risky_mtd))

    ###############base setting################
    plt.figure(figsize=(10, 5), dpi=600)
    ax = plt.subplot()

    ###############draw plot################

    count = collections.Counter(nums)
    lst = [(i,j) for i,j in count.items()]
    lst.sort(key=lambda x:x[0])
    x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", ">10"]

    tmp = [i[1] for i in lst]
    y = []
    _sum = 0
    for index, i in enumerate(lst):
        _sum = sum(tmp[:index+1])
        y.append(_sum/len(nums))

    ax.bar(x, y, width=1, align='center', edgecolor='black', linewidth=1.2, zorder=10, color="#1c9d7b")
    ###############draw grid################

    for i in range(1, 10, 2):
        ax.axhline(i*0.1, linestyle='--', color="#CBCBCB", alpha=0.3)

    plt.yticks(fontsize=22)
    plt.xticks(fontsize=22)
    plt.ylim(0, 1.1)
    plt.ylabel(ylabel="Ratio of Downstream", fontsize=26)
    plt.xlabel(xlabel="#Risky Method", fontsize=26)
    plt.grid(axis="y", alpha=0.4, linewidth=1.5)
    plt.savefig("./RQ1.2_RISKY_FUNCTION.png",bbox_inches='tight')


if __name__ == "__main__":
    draw_bar_plot_downstream_risky_mtd()