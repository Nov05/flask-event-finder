import pandas as pd
import numpy as np

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet 
#nltk.download('wordnet')

from gensim import corpora
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora.dictionary import Dictionary
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

from get_summaries import get_summaries

def tokenizer(doc):
    return [token for token in simple_preprocess(doc) if token not in STOPWORDS]

def tokenizer(doc):
     return [token for token in simple_preprocess(doc) 
             if token not in STOPWORDS]
        
def get_opportunities(keywords_in):
    keywords, opportunities = [], []

############################################################  
# get keywords synonyms
############################################################
    for keyword in keywords_in:
        for syn in wordnet.synsets(keyword):
            for l in syn.lemmas():
                keywords.append(l.name())
    keywords = list(set(keywords))

############################################################  
# get nearest summaries
############################################################  
    summaries = get_summaries()
    summaries = pd.DataFrame(summaries)
    
    vect = TfidfVectorizer(
        tokenizer=tokenizer,
        analyzer='word',
        max_df=0.9,
        min_df=10,)

    # document term matrix
    dtm = vect.fit_transform(summaries[1])

    # Fit on TF-IDF Vectors
    nn = NearestNeighbors(n_neighbors=10, 
                          algorithm='ball_tree')
    nn.fit(dtm)

    # nearest distances 
    doc = [' '.join(keywords_in)]
    dtm_doc = vect.transform(doc)
    nearest = nn.kneighbors(dtm_doc.todense())

    for index in nearest[1][0]:
        opportunities.append(df.iloc[index, 0].tolist())   
                
    return keywords, opportunities
