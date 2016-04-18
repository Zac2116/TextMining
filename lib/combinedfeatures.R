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
tfidf6[,-c(1)],tfidf7[,-c(1,2)],tfidf8[,-c(1,2)],tfidf9[,-c(1,2)],tfidf10[,-c(1,2)])
df[0:10,]
names(df)
names(df) <- c("id",1:30)
head(df)
dim(df)
df <- cbind(tfidf1[,-c(1)],tfidf2[,-c(1,2)],tfidf3[,-c(1,2)],tfidf4[,-c(1,2)],tfidf5[,-c(1,2)],
tfidf6[,-c(1,2)],tfidf7[,-c(1,2)],tfidf8[,-c(1,2)],tfidf9[,-c(1,2)],tfidf10[,-c(1,2)])
dim(df)
names(df) <- c("id",1:30)
head(df)

head(tfidf1)

ts_i <- c(2,5,8)
td_i <- c(3,6)
sd_i <- c(4,7,10,13,16,19,22,25)
formated<-cbind(tfidf1[,2],df[,ts_i],df[,td_i],df[,sd_i])
colnames(formated) <- c("id","ts1_tfidf","ts2_tfidf","ts3_tfidf","td1_tfidf",
                     "td2_tfidf","sd1_tfidf","sd2_tfidf","sd3_tfidf","sd4_tfidf",
                     "sd5_tfidf","sd6_tfidf","sd7_tfidf","sd8_tfidf")

dFeatures <- read.csv("../data/distanceFeatures.csv")

features_tfidf_d <- cbind(dFeatures[,-1],formated[,-1])
write.csv(features_tfidf_d, file = "../data/features_tfidf_d.csv", row.names = FALSE)









