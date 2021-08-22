# coding: utf-8
# ©2021, Jean-Hugues Roy - Licence GNU GPL v3

import csv
import pandas as pan
import spacy
from blabla import mots_vides
from bertopic import BERTopic
from thinc.api import set_gpu_allocator, require_gpu
from flair.embeddings import TransformerDocumentEmbeddings

### Settings for the 1st topic modeling run, using BERTopic with spAcy and these parameters: 30 topics, 2-2 range, top 20 words per topic

spacy.prefer_gpu()
tal = spacy.load("fr_core_news_md", exclude=["tagger","parser","ner","attribute_ruler","lemmatizer"])
modele_thematique = BERTopic(embedding_model=tal, nr_topics=30, n_gram_range=(2,2), top_n_words=20)

### Settings for the 2nd topic modeling run, using BERTopic with spAcy and these parameters: 12 topics, 1-2 range, top 8 words per topic

spacy.prefer_gpu()
tal = spacy.load("fr_core_news_md", exclude=["tagger","parser","ner","attribute_ruler","lemmatizer"])
modele_thematique = BERTopic(embedding_model=tal, nr_topics=12, n_gram_range=(1,2), top_n_words=8, low_memory=True)

### Settings for the 3rd topic modeling run, using BERTopic with FlauBERT and these parameters: 12 topics, 1-2 range, top 8 words per topic

flo = TransformerDocumentEmbeddings("flaubert/flaubert_small_cased")
modele_thematique = BERTopic(embedding_model=flo, nr_topics=12, n_gram_range=(1,2), top_n_words=8, low_memory=True)

### Settings for the 4th topic modeling run, using BERTopic with CamemBERT and these parameters: 12 topics, 1-2 range, top 8 words per topic

cam = TransformerDocumentEmbeddings("camembert-base")
modele_thematique = BERTopic(embedding_model=cam, nr_topics=12, n_gram_range=(1,2), top_n_words=8, low_memory=True)

### The following code works in all runs

francophonie = ["canada","suisse","belgique","france"]
ouinon = ["oui","non"]
lestypes = ["media","nonmedia"]
lesmois = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]

for pays in francophonie:
	fichier = "{0}/{0}-2020-fr-complet-plus100-avec-medias.csv".format(pays)
	fichierOUT = "{}-bertopic.csv".format(pays)
	print(fichier)
	fb = pan.read_csv(fichier, low_memory=False, names=["page","pseudo","fbid","pagelikes","followers","cree","type","likes","comments","partages","love","wow","haha","triste","colere","solidaire","videostatut","videovues","videovuestotales","videovuestotalesallcrosspost","videoduree","url","message","lien","lienfinal","texteimage","textelien","description","interactions","langues","nbcar","media"])
	fb = fb.drop(columns=["videostatut","videovues","videovuestotales","videovuestotalesallcrosspost","videoduree","likes","comments","partages","love","wow","haha","triste","colere","solidaire","pagelikes","followers","langues","lien","lienfinal","nbcar"])
	fb.message = fb.message.fillna("")
	fb.texteimage = fb.texteimage.fillna("")
	fb.textelien = fb.textelien.fillna("")
	fb.description = fb.description.fillna("")

	fb["texte"] = fb.message.str.cat(fb.texteimage, sep=" ").str.cat(fb.textelien, sep=" ").str.cat(fb.description, sep=" ").str.lower()

	fb.texte = fb.texte.apply(lambda x: ' '.join([mot for mot in x.split() if mot not in mots_vides]))

	while "  " in fb.texte:
	    fb.texte.str.replace("  "," ",regex=False)

	fb = fb.drop(columns=['message', 'texteimage', 'textelien', 'description'])

	for m in range(1,13):
		print("{:02d}".format(m))
		mois = fb.cree.str[:7] == "2020-{:02d}".format(m)
		for reponse in ouinon:
			if reponse == "oui":
				med = "media"
			else:
				med = "nonmedia"
			print(reponse)
			letype = fb.media == reponse
			print(fb[mois][letype].shape)
			txt = fb[mois][letype].texte.tolist()
			
			if pays == "france" and reponse == "non": # Section pour le sous-corpus nonmédias de France particulièrement costaud et faisant planter ordi Linux avec GPU!

				moitie = int(len(txt)/2)
				print(moitie)
				for x in range(1,3):
					# print(len(txt))
					if x == 1:
						moitietxt = txt[:moitie]
						print(x,len(moitietxt),type(moitietxt))
					else:
						moitietxt = txt[moitie:]
						print(x,len(moitietxt),type(moitietxt))
				
					themes, probabilites = modele_thematique.fit_transform(moitietxt)
					thematiques = modele_thematique.get_topic_freq().head(21)
				
					for index, thematique in thematiques[1:].iterrows():
						elements = []
						elements.append(pays)
						# elements.append("2020-{:02d}".format(m))
						elements.append("2020-{:02d}-{}".format(m,x)) #ajout pour France
						elements.append(med)
						elements.append(thematique.Count)
						# print(thematique.Count,modele_thematique.get_topic(thematique.Topic))
						for sujet in modele_thematique.get_topic(thematique.Topic):
							elements.append(sujet[0])
							elements.append(sujet[1])
						print(elements)

						sesame = open(fichierOUT, "a")
						street = csv.writer(sesame)
						street.writerow(elements)

			else: # # Section pour les autres sous-corpus
			
				themes, probabilites = modele_thematique.fit_transform(txt)
				thematiques = modele_thematique.get_topic_freq().head(21)

				for index, thematique in thematiques[1:].iterrows():
					elements = []
					elements.append(pays)
					elements.append("2020-{:02d}".format(m))
					# elements.append("2020-{:02d}-{}".format(m,x)) #ajout pour France
					elements.append(med)
					elements.append(thematique.Count)
					# print(thematique.Count,modele_thematique.get_topic(thematique.Topic))
					for sujet in modele_thematique.get_topic(thematique.Topic):
						elements.append(sujet[0])
						elements.append(sujet[1])
					print(elements)

					sesame = open(fichierOUT, "a")
					street = csv.writer(sesame)
					street.writerow(elements)