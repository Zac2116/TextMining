Title: Home Depot Product Search Relevance
==========================================
Group member:
------------------------------------------
* Kewen Zhang, 	  
* Pengfei Wang, 	
* Xiaoci Xing,  	
* Ziyue Wu, 		  

![Click here to read the full report](https://github.com/Zac2116/TextMining/blob/master/doc/FinalReport.pdf)

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

![](https://github.com/Zac2116/TextMining/blob/master/figs/download%20.png)

2. word clouds: 

Search term:

![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/SearchList.png)

Product title:

![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/ProductList.png)

Product Description:

![](https://github.com/Zac2116/TextMining/blob/master/figs/DescriList.png)



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
As most of items have their attributes in data, we choose the most three common attributes among products, brand, color and material.


It's reasonable to compare between search term and these three product attributes.
In this case we used same accard coefficient method. The number of grams here is 1, as many items only have one word in their color and material description.

#### 4. combined features (distance + tf-idf + customized features)
Combined multiply features together.


## Regressor

1. General Linear Model   4201 methods
    * colinearality me

2. Machine Learning Regressor  克文之前做的classifier
    ＊ Cross Validation

3. Neural Network 

- Layers: 4
- Nodes: 50/layers
- Steps: 5000

![](https://raw.githubusercontent.com/Zac2116/TextMining/master/figs/nn_loss.png)

    
## Conclusion

We applied 5-folds cross validation for each regressors to generated the following table:


5-fold CV validated-rMSE comparison:


| Feature\Regressor   | Linear Regression    |Ridge Regression    | RF       | XGB            |
| ------------------- |:--------------------:|:---------------:| -----------:|---------------:|
| Customized      | 0.5329       |0.5329      | 0.5322 	    | 0.5323      |
| Count		   |0.5211	   |0.5211		|0.5143		|0.5154		|
| Distance    | 0.5133      |0.5132         | 0.5100      | 0.5232       |
| Ti-idf | 0.5006        |0.5006         | 0.4968      | 0.4983         |
| All	|	0.4944       |0.4929         | 0.4829      | 0.4829   	     |

## Future work

1. Find better features
2. Increased steps of Neural Network Regressor



