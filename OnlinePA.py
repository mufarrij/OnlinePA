#! /usr/bin/python2.7

import numpy as np
import csv

# Classic Method
def classic(lt, xt):
    return lt / xt


# First Relaxation Method
def first(C, lt, xt):
    return min(C, (lt / xt))


# Second Relaxation Method
def second(C, lt, xt):
    return lt / (xt + (1 / (2 * C)))


# input
train_data = np.loadtxt("data/train_data.csv", dtype='i', delimiter=',')
train_labels = np.loadtxt("data/train_labels.csv", dtype='i', delimiter=',')
test_data=np.loadtxt("data/test_data.csv",dtype='i',delimiter=',')
test_label=np.loadtxt("data/test_labels.csv",dtype='i',delimiter=',')
iterations = 10
C = 1
update_option = 'first'

# PA algoritm
# initiate weight vector
w = np.zeros(9)



#Binary Classification 

for i in range(iterations):
    for index in range(len(train_data)):
        # receive the x instance at time t
        xt = train_data[index, :]
        # predict
        y = train_labels[index] * np.dot(w, xt)
        if y < 1:
            # loss calculation
            lt = max(0, (1 - y))
            xt_square = np.sum(xt ** 2)

            # select the updating option
            if update_option == 'classic':
                tt = classic(lt, xt_square)
            elif update_option == 'first':
                tt = first(C, lt, xt_square)
            else:
                tt = second(C, lt, xt_square)

            # update weights
            w = w + tt * train_labels[index] * xt


#total instances in test_data set
totalraws=len(test_data)

#initiaze correct predictions to zero
count=0

#counting correct predictions
for j in range(totalraws):
         xtt=test_data[j,:]
         pred=np.dot(w,xtt)
         if pred>=1:
            y_h=1
         else:
            y_h=-1

         label=test_label[j]
         
         if label==y_h:
            count=count+1
         

#calculating accuracy of prediction
p=(count/float(totalraws))*100

print "Final Updated Weight  Vector W from Binary Classification PA-",update_option
print "------------------------------------------"
print w
print "------------------------------------------"

print  "for C=",C,"&& for iterations=",iterations 
print  "------------------------------------------"
print  count,"out of",totalraws,"test instances predicted Correctly"
print  "Accuracy in Prediction=",p,"%"


         

