# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:31:02 2021

@author: elois
"""
#Importation of the librairie that we will need in this module
import pandas as pd

#This function takes as input the data base
#This function changes the modalities of the variable named 'defferal_term' by creating a new variable named 'hardhip_plan_binary'
#The variable will takes the value 1 if individuals have experienced a hardship plan
#the value 0 corspond to individuals who have not experienced a hardhip plan
def change_var (df):
    df['deferral_term'].fillna(0,inplace=True)
    df['hardship_plan_binary']=df['deferral_term'].apply(lambda x: 1 if x != 0 else 0)
    del(df['deferral_term'])

#This function takes as input the data base
#It changes the modalities of the variable 'loan_status' thanks to a dictionnary
#The new variable is called 'target'
#The variable takes the value 0 for the individuals which have the old madality 'Fully Paid'
#The value 1 represents the individuals which have the old modality 'Charged Off'
def change_y (data):
    data['target']=data['loan_status']
    replace_map = {'target': {'Fully Paid': 0, 'Charged Off': 1, 
                               'Current':None,
                              'In Grace Period':None, 
                               'Late (31-120 days)':None, 
                               'Late (16-30 days)':None,
                               'Default':None, 
                               'Does not meet the credit policy. Status:Fully Paid':None, 
                               'Does not meet the credit policy. Status:Charged Off':None}}
    data.replace(replace_map, inplace=True)
    del(data['loan_status'])

#This function takes as input the data base 
#It transforme the variable 'issue_d' into a time variable
def change_serietemp (df):
    df['issue_d']=pd.to_datetime(df['issue_d'], format='%b-%Y')

def mise_en_forme (df):
    change_var(df)
    change_serietemp(df)


    
    
  