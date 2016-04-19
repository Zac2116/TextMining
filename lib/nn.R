data <- read.csv("~/Desktop/textMining/data/features_tfidf_d_train.csv")
dim(data)
names(data)
library(neuralnet)

train_index = sample(1:74067,25000)
train_data = data[train_index,]
dim(train_data)
test_data = data[-train_index,]
dim(test_data)

n <- names(train_data[,-1])
f <- as.formula(paste('relevance ~', paste(n[!n %in% 'relevance'], collapse = ' + ')))

nn5 <- neuralnet(f,data = data, hidden = c(5), stepmax = 200000, threshold = 0.3,lifesign = 'full')
glm <- glm(f,data=train_data)

head(test_data)
names(test_data)
compute(nn, test_data[,-1])$net.result
y_hat_nn <- compute(nn24, test_data[,-1])$net.result
mean((y_hat_nn - test_data[,1])^2)

plot(train_data[,3],train_data[,2])


y_hat_glm <- predict(glm,test_data[,c(-1,-2)])
RMSE <- sqrt( mean((y_hat_glm - test_data[,2])^2))

test_data_sub <- read.csv("/Users/zacwu/Desktop/TextMining/data/dfeatures_test.csv")
test_pre <- test_data_sub[,c(-1,-3)]

y_hat_nn24 <- compute(nn24, test_pre[,-1])$net.result
result <- data.frame(id = test_pre[,1],relevance = y_hat_nn24)
write.csv(result, file = "~/Desktop/submission.csv", row.names = FALSE)








