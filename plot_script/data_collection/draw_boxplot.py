import matplotlib.pyplot as plt


def setup():
    all_dict = {}
    with open("downstream/version_count") as f:
        downstream_version_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    with open("upstream/version_count") as f:
        upstream_version_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    all_dict["version_count"] = [downstream_version_count, upstream_version_count]

    with open("downstream/downloaded_count") as f:
        downstream_downloaded_count = [j for j in [max([int(j) for j in i[:-1].split(" ")[1:]]) for i in f.readlines()] if j != 0]
    with open("upstream/downloaded_count") as f:
        upstream_downloaded_count = [j for j in [max([int(j) for j in i[:-1].split(" ")[1:]]) for i in f.readlines()] if j != 0]
    all_dict["downloaded_count"] = [downstream_downloaded_count, upstream_downloaded_count]

    with open("downstream/usage_count") as f:
        downstream_usage_count = [int(i[:-1].split(" ")[1]) for i in f.readlines()]
    with open("upstream/usage_count_lib") as f:
        upstream_usage_count = [int(i[:-1].split(" ")[1]) for i in f.readlines()]
    all_dict["usage_count"] = [downstream_usage_count, upstream_usage_count]

    with open("downstream/class_count") as f:
        downstream_class_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    with open("upstream/class_count") as f:
        upstream_class_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    all_dict["class_count"] = [downstream_class_count, upstream_class_count]

    with open("downstream/method_count") as f:
        downstream_method_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    with open("upstream/method_count") as f:
        upstream_method_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    all_dict["method_count"] = [downstream_method_count, upstream_method_count]

    with open("downstream/loc_count") as f:
        downstream_loc_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    with open("upstream/loc_count") as f:
        upstream_loc_count = [j for j in [int(i[:-1].split(" ")[1]) for i in f.readlines()] if j != 0]
    all_dict["loc_count"] = [downstream_loc_count, upstream_loc_count]

    return all_dict


def draw_all():
    target = list(setup().values())
    title = ["Versions", "Size", "Usage", "Classes", "KLOC"]
    fig, axes = plt.subplots(ncols=5, figsize=(16, 5), constrained_layout=True)

    for i in range(5):
        axes[i].boxplot(target[i], labels=["DOWN", "UP"], sym="r+", showfliers=False, widths=0.7)
        axes[i].set_title(title[i], fontsize=24)
        plt.sca(axes[i])
        plt.xticks(fontsize=24)
        plt.yticks(fontsize=24)
        axes[i].yaxis.get_offset_text().set_fontsize(18)
        axes[i].yaxis.get_offset_text().set_horizontalalignment("center")

    target[-1][1].sort()
    axes[2].set_yticks([1000, 2000, 3000, 4000, 5000], ["1K", "2K", "3K", "4K", "5K"])
    axes[-1].set_yticks([i*2500 for i in range(8)], ["0"]+[str(i*2.5)+"K" for i in range(1, 8)])
    plt.savefig("./data_overview.pdf", dpi=400)


if __name__ == "__main__":
    draw_all()
