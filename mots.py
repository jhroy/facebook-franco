# coding: utf-8
# ©2020, Jean-Hugues Roy - Licence GNU GPL v3

import csv
import spacy
# from collections import Counter

tal = spacy.load("fr_core_news_md")
francophonie = ["canada","suisse","belgique","france"]
fich1 = "motsSeuls.csv"
fich2 = "bigrammes.csv"
fich3 = "trigrammes.csv"
a = b = c = 0

for pays in francophonie:
    fichier = "{0}/{0}-2020-fr-complet-plus100.csv".format(pays)

    f = open(fichier, encoding="utf-8")
    posts = csv.reader(f)
    next(posts)
    # posts = list(posts)
    # print(fichier,len(posts))

    total = n = 0
    tousMots = []
    bigrammes = []
    trigrammes = []

    for post in posts:
        annee = post[5][:4]
        mois = post[5][5:7]
        # print(annee,mois)

        texte = "{} {} {} {}".format(post[22],post[25],post[26],post[27])
        # print(post[25])
        texte = texte.replace("\n", " ")

        while "  " in texte:
            texte = texte.replace("  ", " ")

        texte = texte.strip()

        # print(len(texte),post[-1])

        doc = tal(texte)

        mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False and len(token) > 1 and " " not in token.text and "\n" not in token.text and "http" not in token.text]
        mots = [token.lemma_ for token in doc if token.is_stop == False and \
                    token.is_punct == False and \
                    " " not in token.text and \
                    "http" not in token.text and \
                    ".com" not in token.text and \
                    ".ly" not in token.text and \
                    ".ca" not in token.text and \
                    ".org" not in token.text and \
                    "@" not in token.text and \
                    "\n" not in token.text and \
                    len(token.text) > 1]

        for mot in mots:
            a += 1
            terme1 = [a,mot,pays,post[1],annee,mois,post[28]]
            print(terme1)
            mark = open(fich1, "a")
            zuck = csv.writer(mark)
            zuck.writerow(terme1)

        for x, y in enumerate(mots[:-1]):
            b += 1
            bigramme = "{} {}".format(mots[x], mots[x+1])
            terme2 = [b,bigramme,pays,post[1],annee,mois,post[28]]
            print(terme2)
            mark = open(fich2, "a")
            zuck = csv.writer(mark)
            zuck.writerow(terme2)

        for x, y in enumerate(mots[:-2]):
            c += 1
            trigramme = "{} {} {}".format(mots[x], mots[x+1], mots[x+2])
            terme3 = [c,trigramme,pays,post[1],annee,mois,post[28]]
            print(terme3)
            mark = open(fich3, "a")
            zuck = csv.writer(mark)
            zuck.writerow(terme3)
