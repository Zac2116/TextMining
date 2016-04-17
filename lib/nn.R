train_data <- read.csv("~/Desktop/textMining/data/dfeatures_train.csv")
dim(train_data)
names(train_data)
library(neuralnet)
data = train_data[,-c(1,2)]
head(data)
head(data)
data = train_data[,-c(1,2,4)]
head(data)
dim(data)
dim(data)*0.33
train_index = sample(1:74067,25000)
train_data = data[train_index,]
dim(train_data)
test_data = data[-train_index,]
dim(test_data)

n <- names(train_data)
f <- as.formula(paste('relevance ~', paste(n[!n %in% 'relevance'], collapse = ' + ')))

nn24 <- neuralnet(f,data = data, hidden = c(4,4), stepmax = 200000, threshold = 0.3,lifesign = 'full')
glm <- glm(f,data=train_data)


head(test_data)
names(test_data)
compute(nn, test_data[,-1])$net.result
y_hat_nn <- compute(nn24, test_data[,-1])$net.result
mean((y_hat_nn - test_data[,1])^2)

y_hat_glm <- predict(glm,test_data[,-1])
mean((y_hat_glm - test_data[,1])^2)

test_data_sub <- read.csv("/Users/zacwu/Desktop/TextMining/data/dfeatures_test.csv")
test_pre <- test_data_sub[,c(-1,-3)]

y_hat_nn24 <- compute(nn24, test_pre[,-1])$net.result
result <- data.frame(id = test_pre[,1],relevance = y_hat_nn24)
write.csv(result, file = "~/Desktop/submission.csv", row.names = FALSE)








