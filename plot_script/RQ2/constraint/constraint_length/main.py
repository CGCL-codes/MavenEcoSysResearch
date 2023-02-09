import pickle

from matplotlib import pyplot as plt


def draw_plot(constaint_length_lst: list, cg_length_lst: list):
    constaint_length_lst.sort()
    cg_length_lst.sort()

    num = 0
    x = list(set(constaint_length_lst))
    x.sort()
    y_cons = []
    for i in x:
        for j in constaint_length_lst:
            if j == i:
                num = num + 1
        y_cons.append(num)

    num = 0
    x1 = list(set(cg_length_lst))
    x1.sort()
    y_cg = []
    for i in x1:
        for j in cg_length_lst:
            if j == i:
                num = num + 1
        y_cg.append(num)
    ####################Base setting##########################

    plt.figure(figsize=(5, 4), dpi=1000)
    ax = plt.subplot()
    pos1 = ax.get_position()
    pos2 = [pos1.x0 + 0.02, pos1.y0 + 0.05, pos1.width, pos1.height]                ### Adjust the axis position
    ax.set_position(pos2)

    ####################Axis setting##########################
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.ylabel(ylabel="#Path", fontsize=20)
    plt.xlabel(xlabel="Length", fontsize=20)
    plt.grid(axis="y", alpha=0.4)
    plt.grid(axis="x", alpha=0.4)

    ####################Draw plot##########################

    plt.plot(x, y_cons, label="constraint", zorder=10, color="blue")
    plt.plot(x1, y_cg, label="call graph", color="#555555", linestyle="dashed")
    plt.legend(fontsize=20)

    plt.savefig("./RQ2_constraint_length.png",bbox_inches='tight')

if __name__ == "__main__":
    with open("./raw_data/length_lst", "rb") as f:
        all_length_constraint, all_length_cg = pickle.load(f)

    draw_plot(all_length_constraint, all_length_cg)