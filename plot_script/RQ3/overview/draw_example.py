from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def heat_pic_example():
    begin = datetime(2008, 1, 1)
    end = datetime(2022, 8, 17)
    all_length = (datetime(2022, 8, 17) - datetime(2008, 1, 1)).days
    first_tag = [datetime(2020, 3, 9), datetime(2020, 9, 13)]
    published_time = (datetime(2021,12,28)-begin).days
    commit_time = [datetime(2022, 1, 9), datetime(2022, 5, 30)]
    
    time_1 = [(i-begin).days for i in first_tag]
    time_2 = [(commit_time[0]-begin).days, (commit_time[1]-begin).days]

    base = [110] * all_length
    heat_pic_data = []
    for i in range(750):
        heat_pic_data.append(base[:])
    
    for i in range(375, 750):
        for j in range(time_1[0], time_2[0]):
            heat_pic_data[i][j] = 90
    for i in range(375):
        for j in range(time_1[1], time_2[1]):
            heat_pic_data[i][j] = 90
    for i in range(750):
        for j in range(published_time-10, published_time+10):
            heat_pic_data[i][j] = 0

    plt.grid(which="minor")
    xtick_range = [0, (datetime(2010, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2012, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2014, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2016, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2018, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2020, 1, 1) - datetime(2008, 1, 1)).days, (datetime(2022, 1, 1) - datetime(2008, 1, 1)).days]
    
    plt.xticks(xtick_range, ["2008", "2010", "2012", "2014", "2016", "2018", "2020", "2022"],fontsize=10)

    ax = plt.subplot()
    ax.set_yticks([375], minor=True)
    ax.yaxis.grid(True, which='minor', color="black")
    ytick_range = [190, 565]
    plt.yticks(ytick_range, ["", ""])
    im = plt.imshow(heat_pic_data, cmap="hot", origin="lower")

    plt.text(100, 525, "switcher-client", bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
        )
    plt.text(100, 150, "expense-tally-model", bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
        )

    values = [0, 90, 110]
    colors = [im.cmap(im.norm(value)) for value in values]
    t = ["CVE published", "Affected", "Not affected"]
    patches = [mpatches.Patch(color=colors[i], label=t[i]) for i in range(3)]
    plt.legend(handles=patches, loc="upper left", fontsize=10, bbox_to_anchor=(0.45, 1.1))
    plt.savefig("./example.pdf", bbox_inches="tight", dpi=600)


if __name__ == "__main__":
    heat_pic_example()
