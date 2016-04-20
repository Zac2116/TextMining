Title: Home Depot Product Search Relevance
==========================================
Group member:
------------------------------------------
* Kewen Zhang, 	  Uni: kz2246
* Pengfei Wang, 	Uni: pw2406
* Xiaoci Xing,  	Uni: xx2203
* Ziyue Wu, 		  Uni: zw2338

![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/searchImage.png)

## Quick Summary

Predict relevance scores of a given search keywords to Home Depot products, according to product description and attributes.

#### Galance of the training dataset
![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/raw_data.png)

#### Dataset Dummary: 

1. 74067 observations.
2. relevance from 1 less related to 3 highly relevant.


## Data Cleaning
- Fixed typo: “helloWorld” －> "hello World" 
- Cleaned stop words: delete words like "the", "and"
- Replace synonymous words
- Cleared insignificant punctuation: "#.,"
- Cleared plurality: "feet" -> foot
- Changed to word sterm


Before | After
--- | --- 
BEHR Premium Textured DeckOver 1-gal. #SC-141 Tugboat Wood and Concrete Coating | behr premium textur deck 1-ga sc-141 tugboat wood concret coat


## Exploration 
1. relevance distribution.

2. word clouds for each columns 

3. 


## Feature Extraction

#### 1.distance
We have used Jaccard coefficient 

JaccardCoef(A, B) = |A ∩ B| / |A ∪ B|

to calculate the distance between "Search term", "Product Description" and "Product title" respectively 

##### N-grams, n selection

By comparing the variance of each extracted features from 1 - 10 grams, we have the following analysis:
![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/dfeatures.png)
![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/dfeatures2.png)


#### 2.Cosine Similarity with tf-idf (term frequency - inverse document frequency)
In the case of the term frequency tf(t,d), the simplest choice is to use the raw frequency of a term in a document.
The inverse document frequency is a measure of how much information the word provides, that is, whether the term is common or rare across all documents.

For n-grams selection of tf-idf, we have the similar result as Jaccard Coefficient distance:
![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/tfidf.png)
![](https://github.com/Zac2116/TextMining/blob/master/figs/tfidf2.png)

then, we used cosine similarity to obtain the similarity between "Search term", "Product Description" and "Product title" respectively. 
Cosine Similarity: Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them

#### 3. Customized features

#### 4. combined features (distance + tf-idf)
Combined multiply features together.


## Regressor

1. General Linear Model   4201 methods
    * colinearality me

2. Machine Learning Regressor  克文之前做的classifier
    ＊ Cross Validation

3. Neural Network 
    

    
## Conclusion

We applied 5-folds cross validation for each regressors to generated the following table:


| Feature\Regressor   | GLM                 | ML          | NN             |
| ------------------- |:-------------------:| -----------:|---------------:|
| customized               |                     |               |                |
| Distance            |             |          |  0.52107467047949974              |
| tf-idf              |             |           |  0.51244960232101389           |
| all          |             |          |   0.51147107360201327             |


