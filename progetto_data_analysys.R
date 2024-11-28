rm(list = ls())
data <- read.csv("C:\\Users\\Marco\\Documents\\Uni\\sistemi 2\\progetto\\Impact_of_Remote_Work_on_Mental_Health.csv")
#vediamo le variabili ed il loro tipo
summary(data)

str(data)

#il numero di persone con problemi patologici è un binomiale

#dividiamo il dataset in 2 parti
NW <- data[data$Work_Location == "Onsite",]
HW <- data[data$Work_Location == "Hybrid",]
RW <- data[data$Work_Location == "Remote",]
vn <- rep(0, dim(NW)[1])
vh <- rep(0, dim(HW)[1])
vr <- rep(0, dim(RW)[1])

for(i in 1:length(vn)){

  if(NW$Mental_Health_Condition[i] == "None") vn[i] = 0
  else vn[i] = 1
}
NW$Mental_Health_Condition
for(i in 1:length(vh)){
  if(HW$Mental_Health_Condition[i] == "None") vh[i] = 0
  else vh[i] = 1
}
for(i in 1:length(vr)){
  if(RW$Mental_Health_Condition[i] == "None") vr[i] = 0
  else vr[i] = 1
}
pn <- mean(vn)  
ph <- mean(vh)
pr <- mean(vr)

#possiamo valutare la distribuzione col test del chi-quadro
somma_problemi <- sum(vn) + sum(vh) + sum(vr)
somma_sani <- 5000 - somma_problemi
prob_problemi <- somma_problemi/5000
prob_sani <- somma_sani/5000

pearson <- function(x)
