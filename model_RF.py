# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:57:35 2021

@author: elois
"""
#Importation of the librairies
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

#This function makes a Random forest
def random_forest (X_train, Y_train, X_valid, Y_valid, x_test, y_test):

#We apply the random forest on the train part of our data to train the model 
#We set the number of trees in the forest with the option n_estimator
#We chose 10 to have a good performance without taking too much time 
#max_depth is the parameter that allows us to regulate underfitting and overfitting
    model2=RandomForestClassifier(n_estimators=10,max_depth=35)
    model2= model2.fit(X_train, Y_train)
    Y_pred_rf= model2.predict(X_train)
    
#The same model is applied to the validation in order to compare with the train model 
    model_valid2 = model2.fit(X_valid, Y_valid)
    Y_pred_val_rf=model2.predict(X_valid)

#We use the validation curve to validate our model
    curves = []
    for max_depth in range(1,10) :
        clf = RandomForestClassifier(n_estimators=100,max_depth=max_depth,class_weight='balanced')
        clf = clf.fit(X_train, Y_train)
        acu_train2 = accuracy_score( clf.predict(X_train), Y_train)
        acu_valid2 = accuracy_score( clf.predict(X_valid), Y_valid)
        print("max_depth",max_depth, "accuracy",acu_train2,acu_valid2)
        curves.append((max_depth, acu_train2,acu_valid2, clf) )
    plt.plot ( [c[0] for c in curves], [c[1] for c in curves], label="train")
    plt.plot ( [c[0] for c in curves], [c[2] for c in curves], label="valid")
    plt.legend()

#We apply our model on the test part 
    Prob_test2=model2.predict_proba(x_test)
#We keep the predicted probability only for those with a value of 1 
    Prob_1_test2= Prob_test2[:, 1]
#Creation of the classifier without competence
    ns_probs =[0 for _ in range(len(y_test))]

#The AUC score is calculated:
    auc=roc_auc_score(y_test,Prob_1_test2)
    auc_ns=roc_auc_score(y_test,ns_probs)
    print('AUC: %.2f' % auc)
    print('AUC: %.2f' % auc_ns)

#The ROC curve is represented
    lr_fpr, lr_tpr, _ =roc_curve(y_test,Prob_1_test2)
    ns_fpr, ns_tpr, _ =roc_curve(y_test, ns_probs)
    plt.plot(lr_fpr, lr_tpr, marker='.', label='Random Forest')
    plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()