import matplotlib.pyplot as plt
import pickle


def count_acc_ratio():
    """
    Draw the histogram for access ratio to the RM of downstream APIs.
    :return:
    """

    with open("raw_data/all_ratio", "rb") as f:
        all_ratio = pickle.load(f)

    all_ratio_no_zero = list(filter(lambda x:x!=0, all_ratio))              # Filter all those downstream without access

    ###############base setting################

    plt.figure(figsize=(10, 5), dpi=600)

    ###############draw plot################

    plt.hist(all_ratio_no_zero, bins=25, edgecolor='black', linewidth=1.2, zorder=10, density=True, cumulative=True, color="#1c9d7b")

    ###############draw grid################

    ax = plt.subplot()
    for i in range(8):
        ax.axhline(0.6+i*0.05, linestyle='--', color="#CBCBCB", alpha=0.3)
    plt.grid(axis="y", alpha=0.4, linewidth=1.5)
    plt.yticks(fontsize=22)
    plt.xticks(fontsize=22)
    ##############axis setting###############
    plt.xlabel("Threatened Ratio", fontsize=26)
    plt.ylabel("Ratio of Downstream", fontsize=26)
    plt.ylim(0.6, 1.05)
    plt.yticks([0.6, 0.7, 0.8, 0.9, 1.0])

    plt.savefig("./RQ1.2_RISKY_FUNCTION_ACC.png",bbox_inches='tight')


if __name__ == "__main__":
    count_acc_ratio()