import collections
import pickle

import numpy as np
from matplotlib import pyplot as plt


def draw_plot(all_constraint_variable, all_constraint_return_type, all_constraint_operand):
    variable_count = collections.Counter(all_constraint_variable)
    variable_dict = [(key, value) for key, value in variable_count.items()]
    variable_dict.sort(key=lambda x:-x[1])
    key1 = [i[0] for i in variable_dict]
    sum_ = sum([i[1] for i in variable_dict])
    value1_tmp = [i[1]/sum_ for i in variable_dict]

    rtType_count = collections.Counter(all_constraint_return_type)
    rtType_dict = [(key, value) for key, value in rtType_count.items()]
    rtType_dict.sort(key=lambda x: -x[1])
    key2 = [i[0] for i in rtType_dict]
    sum_ = sum([i[1] for i in rtType_dict])
    value2_tmp = [i[1] / sum_ for i in rtType_dict]

    operand_count = collections.Counter(all_constraint_operand)
    operand_dict = [(key, value) for key, value in operand_count.items()]
    operand_dict.sort(key=lambda x: -x[1])
    key3 = [i[0] for i in operand_dict]
    sum_ = sum([i[1] for i in operand_dict])
    value3_tmp = [i[1]/sum_ for i in operand_dict]


    #####################Base setting###########################

    color_lst = ["#2a76ad", "#1b9ac5", "#23bcbf", "#31d3a7", "#63e394", "#aef07f"]
    plt.figure(dpi=2000, figsize=(2.5, 1))
    ax = plt.subplot()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    pos1 = ax.get_position()
    pos2 = [pos1.x0, pos1.y0 + 0.5, pos1.width, pos1.height / 3.0]
    ax.set_position(pos2)

    ##################Axis setting##############################

    plt.yticks(fontsize=4)
    plt.xticks(fontsize=4)

    #######################Draw plot##########################

    for i in range(len(key1)):
        sum_ = sum(value1_tmp[:i])
        b1 = plt.barh("Variable Type1", value1_tmp[i], label=key1[i], left=np.array(sum_), height=0.8, color=color_lst[i], align="center")

    for i in range(len(key2)):
        sum_ = sum(value2_tmp[:i])
        b2 = plt.barh("Variable Type2", value2_tmp[i], label=key2[i], height=0.8, left=np.array(sum_), color=color_lst[i], align="center")

    for i in range(len(key3)):
        sum_ = sum(value3_tmp[:i])
        b3 = plt.barh("Constraint Operand", value3_tmp[i], label=key3[i], height=0.8, left=np.array(sum_), color=color_lst[i], align="center")

    ####################ledend setting#########################
    font = {
        'size': 4,
    }

    plt.text(-0.11, -3.5, "Variable Type1", fontsize=4)
    plt.text(0.21, -3.5, "Variable Type2", fontsize=4)
    plt.text(0.62, -3.5, "Variable Operand", fontsize=4)
    plt.legend(bbox_to_anchor=(0.9, -1), ncol=4, prop=font)
    plt.savefig("./RQ2_variable_constraint.png", bbox_inches="tight")


if __name__ == "__main__":
    with open("./raw_data/operand_variable", "rb") as f:
        all_constraint_variable, all_constraint_return_type, all_constraint_operand = pickle.load(f)

    draw_plot(all_constraint_variable, all_constraint_return_type, all_constraint_operand)

