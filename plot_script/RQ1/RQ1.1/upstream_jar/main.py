import matplotlib.pyplot as plt
import collections
import pickle


def use_acc_ratio():
    """
    Draw plot for the (downstream can access the vulnerability/downstream use the upstream)
    :return:
    """
    with open("raw_data/commonly_API_acc_ratio", "rb") as f:
        commonly_API_acc_ratio = pickle.load(f)

    with open("raw_data/usage_acc_ratio", "rb") as f:
        usage_acc_ratio = pickle.load(f)

    count = collections.Counter(commonly_API_acc_ratio)
    dd = sorted(count.items(), key=lambda x: x[0])
    x1 = list(set([i[0] for i in dd]))
    x1.sort()
    num = 0
    y1 = []
    for i in x1:
        for j in commonly_API_acc_ratio:
            if j == i:
                num = num + 1
        y1.append(num/len(commonly_API_acc_ratio))

    ###############base setting################

    plt.figure(figsize=(10, 5), dpi=600)
    ax = plt.subplot()

    ###############draw histogram and line################

    plt.hist(usage_acc_ratio, bins=25, edgecolor='black', linewidth=1.2, zorder=10, cumulative=True, density=True, color='#AAAAAA')
    plt.plot(x1, y1, zorder=11, color="blue", linestyle="-", linewidth=2, label="Top-10 API Reachable Ratio")
    plt.legend(loc='upper left', fontsize=20)

    ###############draw grid################

    plt.grid(axis="y")
    ax.axhline(0.65, xmin=0, xmax=1, linestyle="--", color="#CBCBCB", alpha=0.3)
    ax.axhline(0.75, xmin=0, xmax=1, linestyle="--", color="#CBCBCB", alpha=0.3)
    ax.axhline(0.85, xmin=0, xmax=1, linestyle="--", color="#CBCBCB", alpha=0.3)
    ax.axhline(0.95, xmin=0, xmax=1, linestyle="--", color="#CBCBCB", alpha=0.3)
    plt.yticks(fontsize=22)
    plt.xticks(fontsize=22)
    ##############axis setting###############
    plt.xlabel("Affected Ratio", fontsize=26)
    plt.ylabel('Ratio of Upstream', fontsize=26)
    plt.ylim(0.6, 1.08)
    plt.savefig("./RQ1.1_USAGE_ACC_RATIO.png", bbox_inches='tight')


if __name__ == "__main__":
    use_acc_ratio()