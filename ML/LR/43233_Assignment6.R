library("Metrics")
library("DAAG")
library("lattice")
getwd()
df <- read.csv(file.choose())
head(df)
dim(df)
train_dataset=df[1:28,]
head(train_dataset)
test_dataset=df[29:50,]
head(test_dataset)
rd=lm(Profit~R.D.Spend,data=train_dataset)
rd
ad=lm(Profit~Administration,data=train_dataset)
ad
mar=lm(Profit~Marketing.Spend,data=train_dataset)
mar
plot(train_dataset$Profit~train_dataset$R.D,xlab="R.D",ylab = "Profit")
abline(rd)
plot(train_dataset$Profit~train_dataset$Administration,xlab="Administration",ylab = "Profit")
abline(ad)
plot(train_dataset$Profit~train_dataset$Marketing,xlab="Marketing",ylab = "Profit")
abline(mar)
summary(rd)
summary(ad)
summary(mar)
rdp=predict(rd,train_dataset)
adp=predict(ad,train_dataset)
marp=predict(mar,train_dataset)
rdt=predict(rd,test_dataset)
adt=predict(ad,test_dataset)
mart=predict(mar,test_dataset)
rdtrain_mse=mse(train_dataset$R.D,rdp)
rdtrain_mse
adtrain_mse=mse(train_dataset$Administration,adp)
adtrain_mse
martrain_mse=mse(train_dataset$MArketing.Spend,marp)
martrain_mse
rdtest_mse=mse(test_dataset$R.D.Spend,rdt)
rdtest_mse
adtest_mse=mse(test_dataset$Administration,adt)
adtest_mse
martest_mse=mse(test_dataset$Marketing,mart)
martest_mse
TrainMSE=c(rdtrain_mse,adtrain_mse,martrain_mse)  
TrainMSE
TestMSE=c(rdtest_mse,adtest_mse,martest_mse)
TestMSE
barplot(TrainMSE,width = 0.02,xlab="data",ylab="error",main="Training Error")
