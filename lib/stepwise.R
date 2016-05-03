df <- read.csv("~/Desktop/train_allfeature_reborn.csv")
library(leaps)
y <- df[,2]
x <- df[,3:36]
leaps <- regsubsets(y~as.matrix(x),data=df,nbest=10,method = 'backward')
plot(leaps,scale="Cp")
summary(leaps)
back_all <- lm(df$relevance~ts1+ts1_tfidf+ts2_tfidf+td1_tfidf+sd1_tfidf+ProductNum+SearchNum+brandNum,data=df)
summary(back_all)

x1 <- df[,3:15]
leaps1 <- regsubsets(y~as.matrix(x1),data=df,nbest=10,method = 'backward')
plot(leaps1,scale="Cp")

x2 <- df[,16:28]
leaps2 <- regsubsets(y~as.matrix(x2),data=df,nbest=10,method = 'backward')
plot(leaps2,scale="Cp")

#count
x3 <- df[,32:36]
leaps3 <- regsubsets(y~as.matrix(x3),data=df,nbest=10,method = 'backward')
plot(leaps3,scale="Cp")

#customized
x4 <- df[,29:31]
leaps4 <- regsubsets(y~as.matrix(x4),data=df,nbest=10,method = 'backward')
plot(leaps4,scale="Cp")
