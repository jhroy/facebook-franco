# Kittens 😸 and Jesus ✝️ &nbsp;:<br>What Would Remain in a Newsless Facebook

This repository relates to an article published in journal on day month, 202x. 

For this article, I first proceded to extract the 300&nbsp;000 posts which garnered the most attention on pages administered mainly in Belgium, Canada, France and Switzerland for each month of the year 2020. After filtering this 13.4M-post initial sample, as decribed in the article, I kept a final sample of 3.3M posts in French.

One of the steps in the filtering involved determining the language of each post. This was done with the following python script&nbsp;:

- [**langues.py**](langues.py)

The pages in this final sample were then manually classified in two categories (criteria described in the article)&nbsp;: media and non-media. The following four CSV files show how pages were classified in each country, along with the number of posts and sum of interactions from each page (only those posts that were included in my sample)&nbsp;:

- [**belgique2020-pages-fb-fr.csv**](belgique2020-pages-fb-fr.csv) 🇧🇪
- [**canada2020-pages-fb-fr.csv**](canada2020-pages-fb-fr.csv) 🇨🇦
- [**france2020-pages-fb-fr.csv**](france2020-pages-fb-fr.csv) 🇫🇷
- [**suisse2020-pages-fb-fr.csv**](suisse2020-pages-fb-fr.csv) 🇨🇭

Those results are also summarized in the following graph.

![](images/FBfrancophonie-bilan.png)

[CrowdTangle's ToS](https://www.crowdtangle.com/terms/) do not allow the sharing of raw data. However, a summary of interaction types by subcorpora (8 subcorpora in total; one per country and per type [media vs nonmedia]) can be found in the following CSV file&nbsp;:

- [**francophonie2020-sommaire.csv**](francophonie2020-sommaire.csv)

### Step 1 : n-gram extraction

To extract unigrams, bigrams and trigrams from each of the 8 subcorpora, I used this python script&nbsp;:

- [**mots.py**](mots.py)

All n-grams were then cleaned-up (to remove residual punctuation or funky whitespace characters, for example) and uniformized using this script&nbsp;:

- [**nettoyage.py**](nettoyage.py)

The 24 csv files (3 n-gram types * 2 categories * 4 countries) produced by these scripts were between 3.6M and 37.3M lines long. Each lined contained a term and the interaction figure for the post it was found in. To find the frequency of each word and to weigh it by interactions, such as described in the article, a pivot table was performed using pandas. An example of the code used in the case the Belgium corpus CSV files is found in this notebook&nbsp;:

- [**123-grams.ipynb**](123-grams.ipynb)

### Step 2 : chi-squared (χ<sup>2</sup>) residuals

I then proceeded to compare media and non-media unigrams, bigrams and trigrams for each country. This was done in a jupyter notebook for each country, producing graphs with [plotly express for python](https://plotly.com/python/plotly-express/). The raw notebooks are too big to be shared directly in github. They were placed on an personal server in HTML format&nbsp;:

- [**khi2-belgique**](http://jhroy.ca/facebook-franco/khi2-belgique.html)
- [**khi2-canada**](http://jhroy.ca/facebook-franco/khi2-canada.html)
- [**khi2-france**](http://jhroy.ca/facebook-franco/khi2-france.html)
- [**khi2-suisse**](http://jhroy.ca/facebook-franco/khi2-suisse.html)

This step is, IMHO, the most relevant and revealing of a newsless Facebook.

For example, the most characteristic bigrams of the media and non-media canadian subcorpora really show how different Facebook would be without news.

![](images/bigrams-canada-media.png)

![](images/bigrams-canada-nonmedia.png)

### Step 3 : topic modeling

The last step involved an exploratory topic modeling on all 8 subcorpora using [BERTopic](https://maartengr.github.io/BERTopic/index.html) in the following script&nbsp;:

- [**topicBERT.py**](topicBERT.py)

I used BERTopic with three different models&nbsp;:

- [spaCy's ```fr_core_news_md``` model](https://spacy.io/models/fr) (2 runs with different parameters)
- [FlauBERT](https://github.com/getalp/Flaubert)
- [CamemBERT](https://camembert-model.fr/)

The four runs were performed on each month for all 8 suborpora. Since topic modeling is extremely memory intensive, some months had to be cut in two in the case of the non-media French subcorpus. Below are examples of the topics given for the month of June for both media and non-media subcorpora by country and by model.

Topics for **media** subcorpora (June 2020)&nbsp;:

- In Belgium 🇧🇪 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/belgique-spacy1-media-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-spacy2-media-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-flaubert-media-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-camembert-media-2020-06.csv)

- In Canada 🇨🇦 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/canada-spacy1-media-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-spacy2-media-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-flaubert-media-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-camembert-media-2020-06.csv)

- In France 🇫🇷 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/france-spacy1-media-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-spacy2-media-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-flaubert-media-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-camembert-media-2020-06.csv)

- In Switzerland 🇨🇭 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/suisse-spacy1-media-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-spacy2-media-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-flaubert-media-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-camembert-media-2020-06.csv)

Topics for **non-media** subcorpora (June 2020)&nbsp;:

- In Belgium 🇧🇪 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/belgique-spacy1-nonmedia-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-spacy2-nonmedia-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-flaubert-nonmedia-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/belgique-camembert-nonmedia-2020-06.csv)

- In Canada 🇨🇦 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/canada-spacy1-nonmedia-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-spacy2-nonmedia-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-flaubert-nonmedia-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/canada-camembert-nonmedia-2020-06.csv)

- In France 🇫🇷 (here, with the FlauBERT and CamemBERT models, the subcorpus had to be split in half, thus the CSV files contain 24 topics instead of 12:

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/france-spacy1-nonmedia-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-spacy2-nonmedia-2020-06.csv)
  - [As given by the **FlauBERT model** (24 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-flaubert-nonmedia-2020-06.csv)
  - [As given by the **CamemBERT model** (24 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/france-camembert-nonmedia-2020-06.csv)

- In Switzerland 🇨🇭 :

  - [As given by the **first run with spaCy's model** (20 topics, 2 lemmas per term, 20 terms per topic)](berTOPIC/suisse-spacy1-nonmedia-2020-06.csv)
  - [As given by the **second run with spaCy's model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-spacy2-nonmedia-2020-06.csv)
  - [As given by the **FlauBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-flaubert-nonmedia-2020-06.csv)
  - [As given by the **CamemBERT model** (12 topics, 1-2 lemmas per term, 8 terms per topic)](berTOPIC/suisse-camembert-nonmedia-2020-06.csv)

I found CamemBERT produced much more coherent, robust and easy to interpret topics in French.

The following figure, in the article, presents a compound of all 384 tables produced by my topic modeling runs containing more than 5,000 topics.

![](images/Fig5.jpg)
