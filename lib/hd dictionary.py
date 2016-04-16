
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
tokenizer = RegexpTokenizer(r'\w+')
stemmer = SnowballStemmer('english')
st = WordNetLemmatizer()


# # Train

# In[12]:

train=pd.read_csv('train_clean.csv',encoding='ISO-8859-1',keep_default_na=False,na_values=[])


# # TF-IDF

# ## Common Vocabulary

# In[16]:

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df = 0, stop_words = 'english',encoding='ISO-8859-1')


# In[17]:

combineList=(train.productList+train.desList+train.searchList)

# In[21]:

CombineList = pd.Series()
for i in range(len(combineList)):
    CombineList=np.append(CombineList,combineList[i].split())


# # Function

# In[28]:

def df_itf(item,name):
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df = 0, stop_words = 'english')  #at most gram-2
    tfidf_matrix=tf.fit_transform(item)   #item should be pd.Series
    feature_names = tf.get_feature_names()
    dense = tfidf_matrix.todense()
    episode=dense.tolist()[0]  ##
    phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
    train[name]=0
    for i in range(len(dense)):
        aadict = {}
        episode=dense[i].tolist()[0]
        phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
        sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
        for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores]:
            aadict[phrase] = score
            train[name][i] = [aadict]


# In[29]:
## Common dictionary
df_itf(CombineList,'a')

# In[32]:

train.a[:3]


# In[153]:

#Concate the dict matrix
con_matrix=pd.DataFrame()
each_row=pd.DataFrame()
def concate_matrix(item):
    for i in range(len(item)):
        each_row=pd.DataFrame(item[i])
        con_matrix = pd.concat([con_matrix,each_row],ignore_index=True)
        if i>10:
            break


# ### SDT

# In[99]:

import numpy as np
from sklearn.decomposition import TruncatedSVD


# In[100]:

# n_components remains unknown

svd = TruncatedSVD(n_components = 2, n_iter=15)


# In[101]:

result = svd.fit(con_matrix)





# In[ ]:

from sklearn.metrics.pairwise import cosine_similarity


# In[ ]:

cosine_similarity([1,1,1],[2,2,3])

