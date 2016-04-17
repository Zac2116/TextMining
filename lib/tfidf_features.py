from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
#from nltk.corpus import stopwords
def tf_idf_features(train_ls):
    train_set = train_ls #Documents
    vectorizer = CountVectorizer()#stop_words = stopWords
    transformer = TfidfTransformer()
    trainVectorizerArray = vectorizer.fit_transform(train_set).toarray()
    transformer.fit(trainVectorizerArray)
    return transformer.transform(trainVectorizerArray).toarray()

from sklearn.metrics.pairwise import cosine_similarity


def tfidf_cosSim(train):
    df = pd.DataFrame()
        #i = 0
    for i in range(0,len(train)): #len(train)
        id = train.iloc[i]['id']
        t = train.iloc[i]['productList']
        s = train.iloc[i]['searchList']
        d = train.iloc[i]['desList']
        cur_ls = [t,s,d]
        tfidf = tf_idf_features(cur_ls)
        m =  cosine_similarity(tfidf)
        ts = m[0][1]
        td = m[0][2]
        sd = m[1][2]
        df2 = pd.Series([id]+[ts]+[td]+[sd])
        df = df.append(df2, ignore_index=True)
    
    names =['id','ts1','td1','sd1']
    df.columns = names
    return df

