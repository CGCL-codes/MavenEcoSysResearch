import matplotlib.pyplot as plt
import numpy as np
import pickle


with open("./data/distribution", "rb") as f:
    all, with_invocation, direct, transitive, without_invocation = pickle.load(f)

# target_list = [direct, transitive, with_invocation, without_invocation, all]

# labels = ["Direct", "Transitive", "Reachable", "Unreachable", "All"]

target_list = [all, direct, transitive, with_invocation, without_invocation]

labels = ["All", "Direct", "Transitive", "Reachable", "Unreachable"]

# get ratio
for i in target_list:
    i.extend([i[0][0]/(sum(i[0])+i[1]), i[0][1]/(sum(i[0])+i[1]), i[0][2]/(sum(i[0])+i[1]), 1-sum(i[0])/(sum(i[0])+i[1])])
    
update = [i[2] for i in target_list]
downgrade = [i[3] for i in target_list]
alter = [i[4] for i in target_list]
no_response = [-i[-1] for i in target_list]

plt.figure(figsize=(10, 5), dpi=600)

ytick_range = [-0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8]
plt.yticks(ytick_range, ["0.4", "0.2", "0", "0.2", "0.4", "0.6", "0.8"], fontsize=30)

plt.bar(labels, update, label="Upgrade" ,width=0.45, zorder=10, color="#009e79")
plt.bar(labels, downgrade, label="Downgrade", width=0.45, zorder=10, bottom=np.array(update) + np.array(alter), color="red")
plt.bar(labels, alter, label="Remove", width=0.45, zorder=10, bottom=update, color="#333333")
plt.bar(labels, no_response, label="No response", width=0.45, zorder=10, color="#AAAAAA", hatch="xx",edgecolor="white")

plt.ylim(-0.2, 1.0)

plt.ylabel("Response Ratio", fontsize=35)

plt.xlabel("", fontsize=30)
plt.xticks(fontsize=35, rotation=18)

plt.legend(ncol=2, loc='upper center', bbox_to_anchor=(0.45, 1.45), fontsize=32)

plt.grid(axis="y", alpha=0.2, linewidth=1)
plt.grid(axis="x", alpha=0.2, linewidth=1)

plt.savefig("./distribution.pdf", bbox_inches="tight")
