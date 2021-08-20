# License GNU, GPL v3 -- Jean-Hugues Roy -- 2021
# coding: utf-8

import csv, langid, glob
# from textblob import TextBlob
from langdetect import detect
from polyglot.detect import Detector
from collections import Counter

fichiers = []

for fichier in glob.glob("*/*300k-2020-*.csv", recursive=True):
	fichiers.append(fichier)

for fichier in fichiers:
	fichOut = "{}-avec-langues.csv".format(fichier.replace(".csv",""))
	print(fichier,fichOut)

	f = open(fichier)
	posts = csv.reader(f)
	next(posts)

	for post in posts:
		langues = []

		texte = post[22].strip() + " " + post[25] + " " + post[26] + " " + post[27]
		texte = texte.replace("\n"," ")
		while "  " in texte:
			texte = texte.replace("  "," ")
		texte = texte.lower().strip()
		
		print("«")
		print(texte)
		print("»")

		try:
			if texte is not None and texte != "":
				# print(detect(texte))
				langues.append(detect(texte)) # Utilisation de langdetect
				# lang = TextBlob(texte)
				# print(lang.detect_language())
				# langues.append(lang.detect_language())
				# print(langid.classify(texte),type(langid.classify(texte)))
				# for l in langid.classify(texte):
					# print(langid.classify(texte).index(l),l)
				# print(langid.classify(texte)[0])
				langues.append(langid.classify(texte)[0]) # Utilisation de langid
				detecteur = Detector(texte)
				langues.append(detecteur.language.code) # Utilisation de polyglot
				# print(detecteur.language.code)
				print(langues)
				freq = Counter(langues)
				# print(freq.most_common(1)[0][0],freq.most_common(1)[0][1])
				if freq.most_common(1)[0][1] > 1:
					langue = freq.most_common(1)[0][0]
				else:
					langue = "inconnue"
			else:
					langue = "inconnue"
		except:
			langue = "inconnue"
			# print("##############################")
			# print("### Pas pu faire l'analyse ###")
			# print("##############################")
		print(langue)
		print("+"*10)
	
		post.append(langue)

		print(post)

		mark = open(fichOut, "a")
		zuck = csv.writer(mark)
		zuck.writerow(post)