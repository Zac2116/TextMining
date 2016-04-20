library(tm)
library(SnowballC)
library(wordcloud)
library(RColorBrewer)


train <- read.csv("~/Documents/kaggle/homedepot/train_clean.csv",stringsAsFactors = FALSE)
CombineCorpus <- Corpus(VectorSource(train[,7:9]))
CombineList <- tm_map(CombineCorpus, PlainTextDocument)
wordcloud(CombineList, max.words = 100, random.order = FALSE, colors=brewer.pal(8, "Dark2"))

ProductdesCorpus <- Corpus(VectorSource(train$desList))
ProductdesList <- tm_map(ProductdesCorpus, PlainTextDocument)
wordcloud(ProductdesList, max.words = 100, random.order = FALSE, colors=brewer.pal(8, "Dark2"))

SearchCorpus <- Corpus(VectorSource(train$searchList))
SearchList <- tm_map(SearchCorpus, PlainTextDocument)
wordcloud(SearchList, max.words = 100, random.order = FALSE, colors=brewer.pal(8, "Dark2"))

ProductCorpus <- Corpus(VectorSource(train$productList))
ProductList <- tm_map(ProductCorpus, PlainTextDocument)
wordcloud(ProductList, max.words = 100, random.order = FALSE, colors=brewer.pal(8, "Dark2"))
