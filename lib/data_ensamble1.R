tfidf1 <- read.csv("../data/tfidf_1gram.csv")
tfidf2 <- read.csv("../data/tfidf_2gram.csv")
tfidf3 <- read.csv("../data/tfidf_3gram.csv")
tfidf4 <- read.csv("../data/tfidf_4gram.csv")
tfidf5 <- read.csv("../data/tfidf_5gram.csv")
tfidf6 <- read.csv("../data/tfidf_6gram.csv")
tfidf7 <- read.csv("../data/tfidf_7gram.csv")
tfidf8 <- read.csv("../data/tfidf_8gram.csv")
tfidf9 <- read.csv("../data/tfidf_9gram.csv")
tfidf10 <- read.csv("../data/tfidf_10gram.csv")

df <- cbind(tfidf1[,-c(1)],tfidf2[,-c(1,2)],tfidf3[,-c(1,2)],tfidf4[,-c(1,2)],tfidf5[,-c(1,2)],
            tfidf6[,-c(1,2)],tfidf7[,-c(1,2)],tfidf8[,-c(1,2)],tfidf9[,-c(1,2)],tfidf10[,-c(1,2)])

names(df) <- c("id",1:30)

write.csv(df, file = "../output/ngrams_TF.csv", row.names = FALSE)


