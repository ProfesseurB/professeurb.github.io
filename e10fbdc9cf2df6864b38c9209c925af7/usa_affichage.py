# Fichier d'accompagnement

import matplotlib.pyplot as plt

# fonction d'affichage

def affiche_etapes(e):
    for i in range(len(etats_adjacents)):
        for j in etats_adjacents[i]:
            if i <= j:
                x1 = float(etats[i][4])
                y1 = float(etats[i][3])
                x2 = float(etats[j][4])
                y2 = float(etats[j][3])
                plt.plot([x1, x2], [y1, y2], 'k', linewidth=0.1)
    for i in range(len(e)):
        j = e[i]
        if i != j:
            x1 = float(etats[i][4])
            y1 = float(etats[i][3])
            x2 = float(etats[j][4])
            y2 = float(etats[j][3])
            plt.plot([x1, x2], [y1, y2], 'r')
    plt.show()

def itineraire(e, start):
    if e[start] == start:
        return []
    l = []
    curr = start
    while e[curr] != curr:
        l.append("{} ({})".format(etats[curr][2], etats[curr][1]))
        curr = e[curr]
    l.append("{} ({})".format(etats[curr][2], etats[curr][1]))
    return l
