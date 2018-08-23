import sqlite3
import matplotlib.pyplot as plt


def legeleistung_to_int(legeleistung_str):
    return int(legeleistung_str) if legeleistung_str else 0


def plot_rassen(maximum):
    con = sqlite3.connect('huhn.db')
    c = con.cursor()
    c.execute("SELECT kurzname,legeleistung FROM rasse ORDER BY legeleistung DESC")
    huehner = c.fetchall()
    xs = []
    ys = []
    counter = maximum
    letzte_legeleistung = 0


    huehner.sort(key=lambda huhn: legeleistung_to_int(huhn[1]), reverse=True)
    for huhn in huehner:
        print("{}\t{}".format(len(xs) + 1, huhn))
        legeleistung = legeleistung_to_int(huhn[1])
        if counter <= len(xs) and legeleistung < letzte_legeleistung:
            break
        xs.append(huhn[0])
        ys.append(legeleistung)
        letzte_legeleistung = legeleistung
    plt.plot(xs, ys)
    plt.show()

    c.close()
    con.close()

def plot_legeleistung():
    con = sqlite3.connect('huhn.db')
    c = con.cursor()
    c.execute("SELECT legeleistung,COUNT(legeleistung) FROM rasse WHERE legeleistung IS NOT '' GROUP BY legeleistung")
    counts_raw = c.fetchall()
    counts = [(int(x[0]), x[1]) for x in counts_raw]
    counts.sort()
    legeleistung_vergleich_x = [x[0] for x in counts]
    legeleistung_vergleich_y = [x[1] for x in counts]
    plt.plot(legeleistung_vergleich_x, legeleistung_vergleich_y)
    plt.show()
    c.close()
    con.close()

def main():
    plot_rassen(10)
    plot_legeleistung()

if __name__ == '__main__':
    main()
