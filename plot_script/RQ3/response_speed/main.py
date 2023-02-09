import matplotlib.pyplot as plt
import numpy as np


def x_list(x):
    return [i/(x-1) for i in range(x)]


def read_file(file_path):
    with open(file_path) as f:
        lines = [int(i[:-1]) for i in f.readlines() if int(i) > 0]
    return lines


def calculate_time_delta():
    time_total = read_file("./data/all_time_delta.csv")
    time_no_invocation = read_file("./data/not_reachable_time_delta.csv")
    time_direct_invocation = read_file("./data/direct_time_delta.csv")
    time_tran_invocation = read_file("./data/tran_time_delta.csv")
    time_with_invocation = read_file("./data/reachable_time_delta.csv")

    plt.figure(figsize=(10, 8), dpi=600)

    plt.ylabel("Response Time (days)", fontsize=35)

    plt.yticks(fontsize=30)
    plt.xticks(fontsize=30)

    plt.grid(axis="y", alpha=0.2, linewidth=1)
    plt.grid(axis="x", alpha=0.2, linewidth=1)

    plt.plot(x_list(len(time_total)), time_total, linestyle="dashed",color='#333333',linewidth=2,  label="All")
    plt.plot(x_list(len(time_direct_invocation)), time_direct_invocation, linestyle="dashdot",color='#009e79', linewidth=2, label="Direct Invocation")
    plt.plot(x_list(len(time_tran_invocation)), time_tran_invocation, color="blue", linestyle="dotted", linewidth=2, label="Transitive Invocation")
    plt.plot(x_list(len(time_no_invocation)), time_no_invocation, color="orange",linewidth=2,  label="Unreachable")
    
    plt.legend(fontsize=35)

    plt.savefig("./speed_plt.pdf", bbox_inches="tight")


if __name__ == "__main__":
    calculate_time_delta()
