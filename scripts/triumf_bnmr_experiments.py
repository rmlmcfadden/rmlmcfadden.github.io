#!/usr/bin/python3

import requests
import pandas as pd

# public list of triumf experiments
baseurl = "https://mis.triumf.ca/science/experiment/list.jsf"

# we want every MMS experiment
schedule = "View+all"
discipline = "View+all"
status = "View+all"

# make the full url
url = (
    baseurl
    + "?"
    + "schedule="
    + schedule
    + "&"
    + "discipline="
    + discipline
    + "&"
    + "status="
    + status
)

# base url for the webpage of each experiment
expbaseurl = "https://mis.triumf.ca/science/experiment/view/"

# get the page html
html = requests.get(url).content

# extract the table
df_list = pd.read_html(html)
df = df_list[-1]

# print(df)
# df.to_csv("triumf_bnmr_experiments.csv")

# drop NaN containing rows (i.e., ones with missing elements)
df = df.dropna()

# tables can be accessed by the column names:
# "Number", "Title", "Spokespersons"
# print(df['Spokespersons'])

# list of the bnmr experiments
experiments = [
    "M815",
    "M816",
    "M817",
    "S863",
    "S871",
    "M897",
    "M913",
    "S971",
    "S972",
    "M1036",
    "M1040",
    "M1041",
    "M1042",
    "M1093",
    "M1094",
    "M1095",
    "M1100",
    "M1119",
    "M1153",
    "S1155",
    "M1165",
    "M1176",
    "M1226",
    "M1305",
    "M1306",
    "S1329",
    "M1354",
    "M1399",
    "M1401",
    "M1403",
    "M1409",
    "M1414",
    "M1419",
    "M1424",
    "M1426",
    "M1436",
    "M1438",
    "M1465",
    "M1490",
    "M1509",
    "M1530",
    "M1538",
    "M1539",
    "M1562",
    "M1563",
    "M1571",
    "M1587",
    "M1604",
    "M1606",
    "M1674",
    "M1743",
    "M1759",
    "M1760",
    "M1770",
    "M1771",
    "M1814",
    "M1821",
    "M1822",
    "M1828",
    "M1871",
    "M1892",
    "M1902",
    "M1903",
    "M1921",
    "M1929",
    "M1939",
    "M1945",
    "M1960",
    "M1963",
    "M2038",
    "M2045",
    "M2061",
    "M2072",
    "M2078",
    "M2100",
    "M2101",
    "M2167",
    "M2220",
    "M2265",
]

# sort and reorder
"""
experiments = sorted(
    experiments, reverse=True, key=lambda n: int(n.strip("M").strip("S"))
)
"""
experiments = sorted(
    experiments, reverse=False, key=lambda n: int(n.strip("M").strip("S"))
)

#
def md_table_row(number, title, spokespersons):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = "[" + number + "](" + exp_url + ")"
    # format some text for better appearence in html
    # check = ['8Li', 'Li+',]
    # for c in check:
    # create the string for the table row
    # row = '| ' + exp_link + ' | ' + title + ' | ' + spokespersons + ' |'
    row = "| " + exp_link + " | " + title + " |"
    return row


#
def html_table_row(number, title, spokespersons):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = '<a href="' + exp_url + '">' + number + "</a>"
    row = "<tr>\n"
    row += "\t<td>" + exp_link + "</td>\n"
    row += "\t<td>" + title + "</td>\n"
    row += "\t<td>" + spokespersons + "</td>\n"
    row += "</tr>"
    return row


# conveniently print n tabs
def tabs(num_tabs):
    tab_str = ""
    for i in range(num_tabs):
        tab_str += "\t"
    return tab_str


#
def html_table_row_tabs(number, title, spokespersons, tabs):
    # make the link in markdown
    exp_url = "https://mis.triumf.ca/science/experiment/view/" + number
    exp_link = '<a href="' + exp_url + '">' + number + "</a>"
    row = tabs + "<tr>\n"
    row += tabs + "\t<td>" + exp_link + "</td>\n"
    row += tabs + "\t<td>" + title + "</td>\n"
    row += tabs + "\t<td>" + spokespersons + "</td>\n"
    row += tabs + "</tr>\n"
    return row


# fix the formatting of isotopes & chemical compounds
def fix_fmt(string):
    fixed = string
    pairs = [
        ["8Li", "<sup>8</sup>Li"],
        ["9Li", "<sup>9</sup>Li"],
        ["11Li", "<sup>11</sup>Li"],
        ["Li+", "Li<sup>+</sup>"],
        ["20F", "<sup>20</sup>F"],
        ["20Na", "<sup>20</sup>Na"],
        ["20,21,25Na", "<sup>20,21,25</sup>Na"],
        ["31Mg", "<sup>31</sup>Mg"],
        ["75,77,79Ga", "<sup>75,77,79</sup>Ga"],
        ["UBe13", "UBe<sub>13</sub>"],
        ["CO2", "CO<sub>2</sub>"],
        ["Cr2O3", "Cr<sub>2</sub>O<sub>3</sub>"],
        ["LiV2O4", "LiV<sub>2</sub>O<sub>4</sub>"],
        ["SrTiO3", "SrTiO<sub>3</sub>"],
        ["LaAlO3", "LaAlO<sub>3</sub>"],
        ["YBa2Cu3O6+x", "YBa<sub>2</sub>Cu<sub>3</sub>O<sub>6+x</sub>"],
        ["YOxHy", "YO<sub>x</sub>H<sub>y</sub>"],
        ["La2CuO4", "La<sub>2</sub>CuO<sub>4</sub>"],
        ["LaNiO3", "LaNiO<sub>3</sub>"],
        ["Fe1+y(Te1-xSex)", "Fe<sub>1+y</sub>(Te<sub>1-x</sub>Se<sub>x</sub>)"],
        ["LiCoO2", "LiCoO<sub>2</sub>"],
        ["Pr2−xCexCuO4", "Pr<sub>2−x</sub>Ce<sub>x</sub>CuO<sub>4</sub>"],
    ]
    for p in pairs:
        fixed = fixed.replace(p[0], p[1])
    return fixed


"""
# write the list as a html table a file
with open("triumf_bnmr_experiments.html", "w") as fh:
    # write the table
    # fh.write(tabs(0) + "<center>\n")
    # fh.write(tabs(0) + '<table id="experiments">\n')
    fh.write(tabs(0) + "<table>\n")
    # head
    fh.write(tabs(1) + "<thead>\n")
    fh.write(tabs(2) + "<th>Number</th>\n")
    fh.write(tabs(2) + "<th>Title</th>\n")
    fh.write(tabs(2) + "<th>Spokespersons</th>\n")
    fh.write(tabs(1) + "</thead>\n")
    # body
    fh.write(tabs(1) + "<tbody>\n")
    for e in experiments:
        for n, t, s in zip(df["Number"], df["Title"], df["Spokespersons"]):
            if e == n:
                # row = md_table_row(n, t, s)
                # row = tabs(3) + html_table_row(n, t, s)
                row = html_table_row_tabs(n, fix_fmt(t), s, tabs(2))
                fh.write(row)
    fh.write(tabs(1) + "</tbody>\n")
    fh.write(tabs(0) + "\t</table>\n")
    # fh.write(tabs(0) + "</center>\n")
"""


def get_status(experiment):
    url = expbaseurl + experiment
    html = requests.get(url).text
    if "Closed" in html:
        return "Closed"
    elif "Approved" in html:
        return "Approved"
    else:
        return "Unknown"


# write the list to yaml file.
with open("../_data/bnmr/experiments.yaml", "w") as fh:
    for experiment in experiments:
        for number, title, spokespersons in zip(
            df["Number"], df["Title"], df["Spokespersons"]
        ):
            if experiment == number:
                status = get_status(experiment)
                fh.write("- experiment: '%s'\n" % number)
                fh.write("  title: '%s'\n" % fix_fmt(title))
                fh.write("  spokespersons: [%s]\n" % spokespersons.replace("  ", ", "))
                fh.write("  url: '%s%s'\n" % (expbaseurl, number))
                fh.write("  status: '%s'\n" % (status))
