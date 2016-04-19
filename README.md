Title: Home Depot Product Search Relevance
==========================================
Group member:
------------------------------------------
* Kewen Zhang, 	  Uni: kz2246
* Pengfei Wang, 	Uni: pw2406
* Xiaoci Xing,  	Uni: xx2203
* Ziyue Wu, 		  Uni: zw2338


## Objective
What is our goal

## Data Clean
- Fixed typo: “helloWorld” －> "hello World" 
- Cleaned stop words
- Replace synomous words
- Cleared insignificant punctuation
- Cleared plurality 
- Changed to word sterm


Before | After
--- | --- 
BEHR Premium Textured DeckOver 1-gal. #SC-141 Tugboat Wood and Concrete Coating | behr premium textur deck 1-ga sc-141 tugboat wood concret coat


## Exploration 
1. relevance distribution.

2. word clouds for each columns 

3. 


## Feature Extraction

1. count

2. distance

3. tf-idf (term frequency - inverse document frequency)

4. combined features (distance + tf-idf)


## Regressor

1. General Linear Model   4201 methods
    * colinearality me

2. Machine Learning Regressor  克文之前做的classifier
    ＊ Cross Validation

3. Neural Network 

    
## Conclusion




| Feature\Regressor   | GLM                 | ML          | NN             |
| ------------------- |:-------------------:| -----------:|---------------:|
| count               |                     |               |                |
| Distance            |             |          |                |
| tf-idf              |             |           |                |
| tf-idf + d          |             |          |                |


