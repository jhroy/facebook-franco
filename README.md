# Kittens 😸 and Jesus ✝️ &nbsp;:<br>What Would Remain in a Newsless Facebook

This repository relates to an article published in journal on day month, 202x. 

For this article, I first proceded to extract the 300&nbsp;000 posts which garnered the most attention on pages administered mainly in Belgium, Canada, France and Switzerland for each month of the year 2020. After filtering this 13.4M-post initial sample, as decribed in the article, I kept a final sample of 3.3M posts in French.

One of the steps in the filtering involved determining the language of each post. This was done with the following python script&nbsp;:

- [**langues.py**](langues.py)

The pages in this final sample were then manually classified in two categories (criteria described in the article)&nbsp;: media and non-media. The following four CSV files show how pages were classified in each country, along with the number of posts and sum of interactions from each page (only those posts that were included in my sample)&nbsp;:

- [**belgique2020-pages-fb-fr.csv**](belgique2020-pages-fb-fr.csv)
- [**canada2020-pages-fb-fr.csv**](canada2020-pages-fb-fr.csv)
- [**france2020-pages-fb-fr.csv**](france2020-pages-fb-fr.csv)
- [**suisse2020-pages-fb-fr.csv**](suisse2020-pages-fb-fr.csv)

[CrowdTangle's ToS](https://www.crowdtangle.com/terms/) do not allow the sharing of raw data. However, a summary of interaction types by subcorpora (8 subcorpora in total; one per country and per type [media vs nonmedia]) can be found in the following CSV file&nbsp;:

- [**francophonie2020-sommaire.csv**](francophonie2020-sommaire.csv)

### Step 1 : n-gram extraction

To extract unigrams, bigrams and trigrams from each of the 8 subcorpora, I used this python script&nbsp;:

- [**mots.py**](mots.py)

All n-grams were then cleaned-up (to remove residual punctuation or funky whitespace characters, for example) and uniformized using this script&nbsp;:

- [**nettoyage.py**](nettoyage.py)
