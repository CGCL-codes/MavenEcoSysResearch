import numpy as np
import matplotlib.pyplot as plt

# Data
def aware_of_cve():
    states = ["No Response", "Response"]
    sca_list = np.array([44, 29])
    aware_list = np.array([51-44, 31-29])
    not_aware_list = np.array([64-51, 47-31])

    plt.figure(figsize=(6, 1.65), dpi=600)
    y = [0, 0.5]
    b2=plt.barh(y, sca_list, align="center", height=0.38, label="aware (by sca)", color="#009e79")
    b1=plt.barh(y, aware_list, align="center", left=sca_list, height=0.38, label="aware (by others)", color="#AAAAAA")
    b3=plt.barh(y, [-i for i in not_aware_list], height=0.38, label="not aware", color="#333333")
    plt.axvline(x = 0, color='black')
    plt.yticks(y, states, fontsize=16)
    plt.xticks([-10, 0, 10, 20, 30, 40, 50, 60], [10, 0, 10, 20, 30, 40, 50, 60], fontsize=16)
    plt.bar_label(b1, label_type="center", fontsize=16)
    plt.bar_label(b2, label_type="center", fontsize=16)
    plt.bar_label(b3, labels=not_aware_list, label_type="center", fontsize=16, color="white")
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis=u'y', which=u'both', length=0)

    plt.legend(ncol=4, bbox_to_anchor=(1.03, -0.43), )
    plt.savefig("./awareness.pdf", bbox_inches="tight", dpi=600)


def update_reason():
    fig, axes = plt.subplots(2, sharex=True, figsize=(6, 1.5))
    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
    axes[0].tick_params(axis=u'both', which=u'both', length=0)
    axes[1].tick_params(axis=u'y', which=u'both', length=0)
    axes[0].spines["bottom"].set_visible(False)
    
    colors=["#009e79", "#AAAAAA", "orange", "orange","#333333"]
    hatches=["xxxx","xxxx","xxxx","","xxxx"]
    edgecolors=["white", "white","white", "white","none"]
    fontcolor=["black","black","black","black","white"]
    not_upgrade = [18, 9, 4]
    reason_list = ["not maintained", "not affected", "others"]
    
    colors1=["#009e79",  "#AAAAAA", "#333333",] 
    hatches1=["","","","",""]
    edgecolors1=["white","white","none","none","none"]
    fontcolor1=["black","black","white","black","white"]

    for i in range(len(not_upgrade)):
        axes[0].bar_label(axes[0].barh(" ", not_upgrade[i], align="center", left=sum(not_upgrade[:i]), height=0.45, label=reason_list[i],color=colors1[i],hatch=hatches1[i],edgecolor=edgecolors1[i]), label_type="center", fontsize=16,color=fontcolor1[i])

    reason_list = ["security issue", "normal upgrade", "get rid of warning", "compatibility issues", "others"]
    upgrade = [30, 10, 8, 2, 1]
    for i in range(len(upgrade)):
        axes[1].bar_label(axes[1].barh(" ", upgrade[i], align="center", left=sum(upgrade[:i]), height=0.45, label=reason_list[i],color=colors[i],hatch=hatches[i],edgecolor=edgecolors[i]), label_type="center", fontsize=16,color=fontcolor[i])
    
    plt.sca(axes[0])
    plt.yticks(fontsize=16)
    plt.sca(axes[1])
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    axes[0].legend(bbox_to_anchor=(1.0, 1.05), labelspacing = 0.2, )
    axes[1].legend(bbox_to_anchor=(1.03, -0.6), ncol=3, )
    plt.savefig("./reason.pdf", bbox_inches="tight", dpi=600)


def how_find_affected():
    fig, axes = plt.subplots(2, sharex=True, figsize=(6, 1.5))
    for ax in axes:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
    axes[0].tick_params(axis=u'both', which=u'both', length=0)
    axes[1].tick_params(axis=u'y', which=u'both', length=0)
    axes[0].spines["bottom"].set_visible(False)

    colors=["#009e79","#AAAAAA","#AAAAAA","#333333"]
    hatches=["","","xxxx",""]
    edgecolors=["none","none","white","none"]
    fontcolor=["black","black","black","white"]
    reason_list = ["manual analysis", "static analysis"]
    not_upgrade = [13, 1]
    for i in range(len(not_upgrade)):
        axes[0].bar_label(axes[0].barh(" ", not_upgrade[i], align="center", left=sum(not_upgrade[:i]), height=0.1, label=reason_list[i],color=colors[i],hatch=hatches[i]), label_type="center",fontsize=16)
    plt.sca(axes[0])
    plt.yticks(fontsize=16)
    plt.sca(axes[1])
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=14)
    upgrade = [30, 5, 3, 3]
    reason_list = ["manual analysis", "static analysis tools", "dynamic testing tools", "reported by the community"]
    for i in range(len(upgrade)):
        axes[1].bar_label(axes[1].barh(" ", upgrade[i], align="center", left=sum(upgrade[:i]), height=0.1, label=reason_list[i],color=colors[i],hatch=hatches[i],edgecolor=edgecolors[i]), label_type="center", fontsize=16, color=fontcolor[i])
    axes[1].legend(loc='lower center',ncol=2, bbox_to_anchor=(0.5,-1.7), )
    plt.savefig("./how_find_affected.pdf", bbox_inches="tight", dpi=600)


# three figs of survey
if __name__ == "__main__":
    aware_of_cve()
    how_find_affected()
    update_reason()