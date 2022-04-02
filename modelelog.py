# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:50:46 2021

@author: elois
"""
#Importation of the librairies
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

#This function makes a Logistic model
def logistic_modele (X_train, Y_train, X_valid, Y_valid, x_test,y_test) :
    
#We apply the logit model on the train part of our data to train the model 
#The solver is used to find the parameter weights that minimize a cost function
#The penalty l2 makes it possible to minimize the cost function. 
#We use the newton-cg solver which is an algorithm that uses gradient descent to minimize the cost function 
#The max_iter corresponds to the maximum number of iterations before converging, we have chosen 65
    model = LogisticRegression(solver='newton-cg',max_iter=65, penalty='l2')
    model = model.fit(X_train, Y_train)
    Y_pred= model.predict(X_train)
    
#The same model is applied to the validation in order to compare with the train model
    model_valid = model.fit(X_valid, Y_valid)
    Y_pred_val=model.predict(X_valid)

#We use the validation curve to validate our model
    curves = []
    for max_iter in range(1,101) :
        RL = LogisticRegression(solver='newton-cg',max_iter=max_iter, penalty='l2')
        RL = RL.fit(X_train, Y_train)
        acu_train = accuracy_score(RL.predict(X_train), Y_train)
        acu_valid= accuracy_score(RL.predict(X_valid), Y_valid)
        print("max_int",max_iter, "accuracy",acu_train,acu_valid)
        curves.append((max_iter,acu_train,acu_valid,RL) )
    plt.figure(figsize=(20,10))
    plt.plot ( [c[0] for c in curves], [c[1] for c in curves], label="train")
    plt.plot ( [c[0] for c in curves], [c[2] for c in curves], label="valid")
    plt.legend()

#We apply our model on the test part 
    Prob_test=model.predict_proba(x_test)
#We keep the predicted probability only for those with a value of 1 
    Prob_1_test= Prob_test[:, 1]
#Creation of the classifier without competence
    ns_probs =[0 for _ in range(len(y_test))]
    
#The AUC score is calculated:
    auc=roc_auc_score(y_test,Prob_1_test)
    auc_ns=roc_auc_score(y_test,ns_probs)
    print('AUC: %.2f' % auc)
    print('AUC: %.2f' % auc_ns)

#The ROC curve is represented
    lr_fpr, lr_tpr, _ =roc_curve(y_test,Prob_1_test)
    ns_fpr, ns_tpr, _ =roc_curve(y_test, ns_probs)
    plt.plot(lr_fpr, lr_tpr, marker='.', label='Logistic')
    plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()
