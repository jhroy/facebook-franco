# coding: utf-8
# ©2021, Jean-Hugues Roy - Licence GNU GPL v3

import csv, unicodeblock.blocks

francophonie = ["canada","suisse","belgique","france"]
ngrams = ["motsSeuls","bigrammes","trigrammes"]
types = ["media","nonmedia"]

def nettoyage(t):
    # print(t)
    t = t.replace("!","")\
    .replace('"','').replace("–","")\
    .replace("(","").replace(")","")\
    .replace(".","").replace(",","")\
    .replace(":","").replace(";","")\
    .replace("+","").replace("=","")\
    .replace("•","").replace("*","")\
    .replace(">","").replace("<","")\
    .replace("&","").replace("$","")\
    .replace("--","-").replace("?","")\
    .replace("|","").replace("~","")\
    .replace("[","").replace("]","")\
    .replace("{","").replace("}","")\
    .replace("/","").replace("_","")\
    .replace("—","-").replace("_","")\
    .lower()
    while t.startswith("-"):
        t = t[1:]
    while t.endswith("-"):
        t = t[:-2]

    # print(t)

    nouveauterme = ""

    for x in t:
        if unicodeblock.blocks.of(x) is not "COMBINING_DIACRITICAL_MARKS"\
        and unicodeblock.blocks.of(x) is not "COMBINING_MARKS_FOR_SYMBOLS"\
        and unicodeblock.blocks.of(x) is not "GENERAL_PUNCTUATION"\
        and unicodeblock.blocks.of(x) is not "IPA_EXTENSIONS"\
        and unicodeblock.blocks.of(x) is not "TAGS"\
        and unicodeblock.blocks.of(x) is not "SPACE"\
        and unicodeblock.blocks.of(x) is not "MATHEMATICAL_ALPHANUMERIC_SYMBOLS"\
        and unicodeblock.blocks.of(x) is not "MATHEMATICAL_OPERATORS"\
        and unicodeblock.blocks.of(x) is not "GEOMETRIC_SHAPES"\
        and unicodeblock.blocks.of(x) is not None\
        and unicodeblock.blocks.of(x) is not "VARIATION_SELECTORS"\
        and unicodeblock.blocks.of(x) is not "PHONETIC_EXTENSIONS"\
        and unicodeblock.blocks.of(x) is not "ARROWS"\
        and unicodeblock.blocks.of(x) is not "SUPPLEMENTAL_ARROWS_B"\
        and unicodeblock.blocks.of(x) is not "SPACING_MODIFIER_LETTERS"\
        and unicodeblock.blocks.of(x) is not "LATIN_EXTENDED_D"\
        and unicodeblock.blocks.of(x) is not "LATIN_1_SUPPLEMENT"\
        and unicodeblock.blocks.of(x) is not "LETTERLIKE_SYMBOLS"\
        and unicodeblock.blocks.of(x) is not "ARABIC_PRESENTATION_FORMS_A"\
        and unicodeblock.blocks.of(x) is not "ARABIC_PRESENTATION_FORMS_B"\
        and unicodeblock.blocks.of(x) is not "NUMBER_FORMS"\
        and unicodeblock.blocks.of(x) is not "CURRENCY_SYMBOLS"\
        and unicodeblock.blocks.of(x) is not "MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS"\
        and unicodeblock.blocks.of(x) is not "ALPHABETIC_PRESENTATION_FORMS"\
        and unicodeblock.blocks.of(x) is not "HALFWIDTH_AND_FULLWIDTH_FORMS"\
        and unicodeblock.blocks.of(x) is not "FULLWIDTH_LATIN "\
        and unicodeblock.blocks.of(x) is not "CJK_SYMBOLS_AND_PUNCTUATION "\
        and unicodeblock.blocks.of(x) is not "SUPERSCRIPTS_AND_SUBSCRIPTS"\
        and unicodeblock.blocks.of(x) is not "SMALL_FORM_VARIANTS"\
        and unicodeblock.blocks.of(x) is not "PRIVATE_USE_AREA":
        # print(x)
            nouveauterme += x

    if len(nouveauterme) == len(t):
        nouveauterme = t

    # print(nouveauterme)
    return(nouveauterme)

for pays in francophonie:
    for ngram in ngrams:
        for typ in types:
            n = nn = 0
            fichierIN = "{0}/{0}-{1}-{2}.csv".format(pays,ngram,typ)
            fichierOUT = "{0}/{0}-{1}-{2}-nettoye.csv".format(pays,ngram,typ)

            print(fichierIN)

            f = open(fichierIN, encoding="utf-8")
            lignes = csv.reader(f)

            blocs = []
            longueur = 0

            for ligne in lignes:
                n += 1
                if ngram == "bigrammes":
                    termes = ligne[0].split()
                    # print(termes)
                    if len(termes) == 2:
                        t1 = nettoyage(termes[0]).strip()
                        # print(t1)
                        t2 = nettoyage(termes[1]).strip()
                        # print(t2)
                    if len(t1) > 0 and len(t2) > 0:
                        nouveau2gram = "{} {}".format(t1,t2)
                        # print(ligne,nouveau2gram)
                        nn += 1

                        print(n,nn,pays[:3],ngram[:3],typ[:3],[nouveau2gram,int(ligne[-1])])

                        mark = open(fichierOUT, "a")
                        zuck = csv.writer(mark)
                        zuck.writerow([nouveau2gram,int(ligne[-1])])

                elif ngram == "trigrammes":
                    # print(ligne)
                    termes = ligne[0].split()
                    if len(termes) == 3:
                        t1 = nettoyage(termes[0]).strip()
                        t2 = nettoyage(termes[1]).strip()
                        t3 = nettoyage(termes[2]).strip()
                    # else:
                        # print(ligne)
                    if len(t1) > 0 and len(t2) > 0 and len(t3) > 0:
                        nouveau3gram = "{} {} {}".format(t1,t2,t3)
                        # print(ligne,nouveau3gram)
                    # else:
                    #     print(ligne)
                        nn += 1

                        print(n,nn,pays[:3],ngram[:3],typ[:3],[nouveau3gram,int(ligne[-1])])
                        
                        mark = open(fichierOUT, "a")
                        zuck = csv.writer(mark)
                        zuck.writerow([nouveau3gram,int(ligne[-1])])

                else:
                    t1 = nettoyage(ligne[0]).strip()
                    if len(t1) > 0:
                        nouveau1gram = t1
                        # print(ligne,nouveau1gram)
                    # else:
                    #     print(ligne)
                    # nouvellepaire = [nouveau1gram,ligne[-1]]
                        nn += 1

                        print(n,nn,pays[:3],ngram[:3],typ[:3],[nouveau1gram,int(ligne[-1])])

                        mark = open(fichierOUT, "a")
                        zuck = csv.writer(mark)
                        zuck.writerow([nouveau1gram,int(ligne[-1])])
                
         
