import pickle
import matplotlib.pyplot as plt
import numpy as np


def draw_mtd_acc_plot():
    """
    Draw the plot for vulnerable functions with different modifier.
    :return:
    """

    with open("./raw_data/vul_function_data", "rb") as f:
        dir_acc_data, tran_acc_data, none_acc_data = pickle.load(f)


    labels = ["final", "default", "protected", "static", "private", "public", "all"]
    dir_acc_data_ratio = np.array(dir_acc_data) / (np.array(dir_acc_data)+np.array(tran_acc_data)+np.array(none_acc_data))
    tran_acc_data_ratio = np.array(tran_acc_data) / (np.array(dir_acc_data)+np.array(tran_acc_data)+np.array(none_acc_data))
    none_acc_data_ratio = np.array(none_acc_data) / (np.array(dir_acc_data)+np.array(tran_acc_data)+np.array(none_acc_data))

    all_mtd_num = np.array(dir_acc_data) + np.array(tran_acc_data) + np.array(none_acc_data)

    ne_dir_acc_data_ratio = -1 * dir_acc_data_ratio
    ne_tran_acc_data_ratio = -1 * tran_acc_data_ratio

    ###############base setting################

    font = {
        'size': 5,
    }
    plt.figure(figsize=(10, 5), dpi=600)

    ###############draw histogram################

    plt.bar(labels, ne_dir_acc_data_ratio, bottom=np.array(ne_tran_acc_data_ratio),
            label="Direct", color="#333333", width=0.45, zorder=10)
    plt.bar(labels, ne_tran_acc_data_ratio, label="Transitive", color="#BBBBBB",
            width=0.45, zorder=10)
    plt.bar(labels, none_acc_data_ratio, label="No", color="#009e79", width=0.45, zorder=10)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fontsize=18)

    ###############x axis setting################



    ###############y axis setting################

    ax = plt.subplot()
    ytick_range = [-0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0]
    plt.yticks(ytick_range, ["0.4", "0.2", "0", "0.2", "0.4", "0.6", "0.8", "1.0"])
    plt.yticks(fontsize=22)
    plt.xticks(fontsize=17)
    plt.ylim(bottom=-0.3, top=1.08)
    ax.set_ylabel("Reachable Ratio", fontsize=25)

    ###############draw grid################

    ax.axhline(-0.1, linestyle='--', color="#CBCBCB", alpha=0.3)
    for i in range(1,10,2):
        ax.axhline(i*0.1, linestyle='--', color="#CBCBCB", alpha=0.3)
    plt.grid(axis="y", alpha=0.4)
    plt.grid(axis="x", alpha=0.4)

   ###############second y axis setting################

    ax2 = ax.twinx()
    ax2.plot(labels, all_mtd_num,  linestyle='dashed', label="#Vulnerable function", linewidth=2, color='blue')
    plt.legend(loc='upper left', fontsize=15)
    plt.yscale("log")
    plt.yticks(fontsize=22)
    ax2.set_ylabel("#Vulnerable Function", fontsize=25)

    plt.savefig("./RQ1.1_MTD.pdf", bbox_inches='tight')


if __name__ == "__main__":
    draw_mtd_acc_plot()