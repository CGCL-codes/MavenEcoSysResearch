import collections
import pickle

from matplotlib import pyplot as plt


def draw_hist(all_constraint_variable:list):
    count = collections.Counter(all_constraint_variable)
    num = len(all_constraint_variable)
    count = [(key, value) for key, value in count.items()]
    count.sort(key=lambda x: x[1])

    x = [i[0] for i in count]
    y = [i[1]/num for i in count]

    x_new = []
    for i in x:
        str_ = "<"
        if i[0] == "0":
            str_ += "NG"
        else:
            str_ += "G"
        str_ = str_ + ","
        if i[1] == "0":
            str_ += "NR"
        else:
            str_ += "R"
        str_ = str_ + ","
        if i[2] == "0":
            str_ += "NP"
        else:
            str_ += "P"
        str_ = str_ + ">"
        x_new.append(str_)

    ###################Base setting#################

    plt.figure(figsize=(10, 4), dpi=600)

    ###################Axis setting#################

    plt.grid(axis="y", alpha=0.4)
    plt.yscale("log")

    ###################Draw plot#################
    plt.bar(x_new, y, zorder=10, color="#AAAAAA")
    plt.yticks(fontsize=18)
    plt.xticks(fontsize=18,rotation=15)
    plt.ylabel("Ratio", fontsize=18)
    plt.savefig("./RQ2_client_acc_patter.pdf", bbox_inches='tight')


if __name__ == "__main__":
    with open("./raw_data/downstream_ctx", "rb") as f:
        all_ctx_pattern = pickle.load(f)
    draw_hist(all_ctx_pattern)