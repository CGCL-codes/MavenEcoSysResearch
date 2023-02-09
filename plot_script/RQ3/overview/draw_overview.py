import csv
import ast
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import requests


def get_cve_published_time_to_file(cve_id):
    with open("./data/CVE_published_time") as f:
        lines = [line[:-1].split(" ") for line in f.readlines()]
    for line in lines:
        if line[0] == cve_id:
            return line[1]
    url = "https://services.nvd.nist.gov/rest/json/cve/1.0/"
    cve_url = url + cve_id
    cve_response = requests.get(cve_url)
    if cve_response.status_code != 200:
        print(cve_id, cve_response.status_code)
        return None
    cve_json = cve_response.json()
    cve_published_time = cve_json["result"]["CVE_Items"][0]["publishedDate"]
    with open("./data/CVE_published_time", "a") as f:
        print(cve_id, cve_published_time, file=f)
    return cve_published_time

        
def draw_overview_fig():
    heat_pic_data = []
    with open("./data/hot_pic.csv") as f:
        reader = csv.reader(f)
        cve_pair_all = []
        for cve_pair in reader:
            cve_pair_all.append(cve_pair)
        cve_pair_all.sort(key=lambda x: get_cve_published_time_to_file(x[0]))
        for cve_pair in cve_pair_all:
            cve_published_time = get_cve_published_time_to_file(cve_pair[0])
            try:
                heat_block = ast.literal_eval(cve_pair[-1])
                if heat_block[0].endswith("n"):
                    heat_block = heat_block[1:]
                heat_list = get_heat_list(heat_block, cve_published_time)
                if heat_list is not None:
                    heat_pic_data.append(heat_list)
            except SyntaxError:
                pass

    plt.figure(figsize=(10, 0.5), dpi=600)
    plt.figure(figsize=(10, 5), dpi=600)
    xtick_range = [0, 365*2, 365*2*2, 365*2*3, 365*2*4, 365*2*5, 365*2*6, 365*2*7]
    plt.xticks(xtick_range, ["2008", "2010", "2012", "2014", "2016", "2018", "2020", "2022"],fontsize=18)

    plt.xlabel("Timeline (year)", fontsize=18)
    plt.ylabel("CVE-Downstream Pair Index", fontsize=18)
    ytick_range = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000]
    plt.yticks(ytick_range, ["", "1K", "2K", "3K", "4K", "5K", "6K", "7K"], fontsize=18)
    im = plt.imshow(heat_pic_data, cmap="hot", origin="lower", aspect="auto")

    values = [20, 90, 110]
    colors = [im.cmap(im.norm(value)) for value in values]
    t = ["CVE published", "Affected", "Not affected"]
    patches = [mpatches.Patch(color=colors[i], label=t[i]) for i in range(3)]
    plt.legend(handles=patches, loc="upper left", fontsize=18)
    plt.savefig("./overview.pdf", bbox_inches="tight")
    

def get_heat_list(heat_block, cve_published_time):
    heat_block = [datetime.strptime(i[:i.find("T")], "%Y-%m-%d") for i in heat_block]
    heat_block = [datetime(2008, 1, 1)] + heat_block + [datetime(2022, 8, 17)]
    res = []
    cve_time_delta = (datetime.strptime(cve_published_time[:cve_published_time.find("T")], "%Y-%m-%d") - datetime(2008, 1, 1)).days

    for i in range(len(heat_block))[:-1]:
        res.append((heat_block[i+1]-heat_block[i]).days)
    order = 110
    final_res = []
    for i in res:
        final_res += [order]*i
        order = 150 - order
    if len(final_res) == 5342:
        for i in range(cve_time_delta-5, cve_time_delta+5):
            final_res[i] = 20
        return final_res
    return None


if __name__ == "__main__":
    draw_overview_fig()
