from huhn import huhnparser as hp

websites = ['https://de.wikipedia.org/wiki/Liste_von_H%C3%BChnerrassen']
min_legeleistung = 0

for website in websites:
    tabelle = hp.parse_huhn_table_from(website)
    huehner = []
    if 0 < len(tabelle):
        huehner = hp.parse_merkmale_from(tabelle)
    else:
        print("[ERROR]\t:\tKeine Tabelle gefunden auf {}".format(website))

    max_huehner, max_legeleistung = hp.get_huhn_mit_max_legeleistung(huehner)
    print("{} Eier werden gelegt von {}\n".format(max_legeleistung,",".join([huhn.merkmale["Name"] for huhn in max_huehner])))

    min_huehner = hp.get_huhn_mit_min_legeleistung(huehner, min_legeleistung)

    print("\n".join(hp.get_huehner_graph(sorted(min_huehner,key=lambda huhn:huhn.merkmale["legeleistung"],reverse=True))))