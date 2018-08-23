import requests
from bs4 import BeautifulSoup
import re

__legeleistung_regex = "\d*"
__legeleistung_parser = re.compile(__legeleistung_regex)

__kurzname_regex = "^[\w\s]*\w"
__kurzname_parser = re.compile(__kurzname_regex)

class Entity():
    def __init__(self):
        self.merkmale = {}
    pass

class __Huehnerrasse(Entity):
    pass

def parse_huhn_table_from(website):
    response = requests.get(website)
    if 200 == response.status_code:
        parsedHtml = BeautifulSoup(response.content, 'html.parser')
        tables = parsedHtml.find_all("table")
    if (len(tables) > 1):
        print("[WARN]\t:\tThere is not 1 but {} tables".format(len(tables)) )
    return tables[0]

def parse_merkmale_from(table):
    rows = table.find_all("tr")
    header_raw = rows[0]
    # remove header from rows
    del rows[0]
    header = [x.text.strip().replace("-", "") for x in header_raw.find_all("th")]
    huehner = []
    for row in rows:
        row_content = row.find_all("td")
        huhn = __Huehnerrasse()
        if ("ohne Großform" == row_content[0].text.strip()):
            __set_zwergrasse(header, huhn, row_content)
        else:
            __set_grossrasse(header, huhn, row_content)
        huehner.append(huhn)
    return huehner

def __parse_legeleistung(legeleistung_raw):
    return int(__legeleistung_parser.search(legeleistung_raw).group())

def __parse_kurzname(name_raw):
    return __kurzname_parser.search(name_raw).group()

def __set_grossrasse(header, huhn, row_content):
    for i in range(len(header)):
        value = row_content[i].text.strip()
        column = str(header[i])
        if (column.startswith("Urzwerg")):
            huhn.merkmale["urzwerg"] = '' if value in ['-', '?', '–'] else value
        else:
            huhn.merkmale[column] = '' if value in ['-', '?', '–'] else value
    huhn.merkmale["kurzname"]=__parse_kurzname(huhn.merkmale["Name"])


def __set_zwergrasse(header, huhn, row_content):
    huhn.merkmale[header[0]] = row_content[8].text.strip()
    huhn.merkmale["legeleistung"]=''
    huhn.merkmale["kurzname"] = __parse_kurzname(huhn.merkmale[header[0]])
    for i in range(1, len(header)):
        column = header[i]
        if (column.startswith("Urzwerg")):
            huhn.merkmale["urzwerg"] = ''
        else:
            huhn.merkmale[column] = ''

def get_huhn_mit_max_legeleistung(huehner):
    max_huehner = []
    parser = re.compile(__legeleistung_regex)
    max_legeleistung = 0
    for huhn in huehner:
        legeleistung_raw = huhn.merkmale["Legeleistungpro Jahr"]
        if legeleistung_raw:
            if not max_huehner:
                max_huehner.append(huhn)
            else:
                legeleistung = __parse_legeleistung(legeleistung_raw)
                if legeleistung == max_legeleistung:
                    max_huehner.append(huhn)
                elif legeleistung > max_legeleistung:
                    max_huehner = [huhn]
                    max_legeleistung = legeleistung
    return max_huehner, max_legeleistung

def get_huhn_mit_min_legeleistung(huehner,min_legeleistung):
    max_huehner = []
    for huhn in huehner:
        legeleistung_raw = huhn.merkmale["Legeleistungpro Jahr"]
        if legeleistung_raw:
            legeleistung = int(__legeleistung_parser.search(legeleistung_raw).group())
            if legeleistung >= min_legeleistung:
                huhn.merkmale["legeleistung"] = legeleistung
        else:
            huhn.merkmale["legeleistung"] = ''
        max_huehner.append(huhn)

    return max_huehner

def get_huehner_graph(huehner):
    x = [huhn.merkmale["Name"] for huhn in huehner]
    y = [int(int(huhn.merkmale["legeleistung"])/10) for huhn in huehner]
    lines = []
    for i in range(len(huehner)):
        if y[i] > 0:
            token = "#"
            amount = ''
            for j in range(y[i]):
                amount = amount + token
            lines.append("{:60}:\t{} ({})".format(huehner[i].merkmale["kurzname"],amount,huehner[i].merkmale["legeleistung"]))
    return lines