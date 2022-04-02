# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:14:57 2021

@author: elois
"""

# Importation of the librairies used
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


######################"DATA VISUALISATION"##################################

############################################################################  
#### Graph 1 : The number of loans depending on the status and the term ####
############################################################################

def cat(df):
    
    # Representation of the loans term depending on the target
    x=sns.catplot(data=df, x='target', kind='count', col='term')
    print(x)


##############################################################################  
############## Graph 2 : The home status of borrower #########################
##############################################################################

def home_status(df):
    
    # Graph's title and axess
    fig, axes = plt.subplots(1,1, figsize=(12,8))
    fig.suptitle('home_ownership status of borrower', fontsize=15)
    
    # Define each of our modalities for the variable that gives information
    # about the borrower'home 
    MORTGAGE=df[df['home_ownership']=='MORTGAGE']
    RENT=df[df['home_ownership']=='RENT']
    OWN=df[df['home_ownership']=='OWN']
    ANY=df[df['home_ownership']=='ANY']
    OTHER=df[df['home_ownership']=='OTHER']
    NONE=df[df['home_ownership']=='NONE']
    
    # Representation with a stack option for each of our modalities 
    sns.histplot(MORTGAGE,x='home_ownership',stat='density',hue='target',multiple="stack")
    sns.histplot(RENT,x='home_ownership',stat='density',hue='target',multiple="stack")
    sns.histplot(OWN,x='home_ownership',stat='density',hue='target',multiple="stack")
    sns.histplot(ANY,x='home_ownership',stat='density',hue='target',multiple="stack")
    sns.histplot(OTHER,x='home_ownership',stat='density',hue='target',multiple="stack")
    sns.histplot(NONE,x='home_ownership',stat='density',hue='target',multiple="stack")
    print(fig)
    
############################################################################## 
########### Graph 3 : The application type of the borrowers ##################
##############################################################################

def app_type(df):
    
    # Graph's title and axes
    fig2, axes = plt.subplots(1,1, figsize=(12,8))
    fig2.suptitle('Application type according status of loan', fontsize=15)
    
    # Define two variables depending on its modalities
    # whether or not the application type was individual or with other applicant
    ap_I=df[df['application_type']=='Individual']
    ap_J=df[df['application_type']=='Joint App']
   
    # Representation with a stack option for each of our modalities 
    sns.histplot(ap_I,x='application_type',stat='density',hue='target',multiple="stack")
    sns.histplot(ap_J,x='application_type',stat='density',hue='target',multiple="stack")
    print(fig2)


############################################################################## 
### Graph 4 : The variation of interest rate according to the loan status ####
##############################################################################

def var_int(df):
    
    # Graph's title and options
    plt.figure(figsize=(8,6))
    plt.title("Variation of interest rate", fontsize=16)
    
    # Representation of the interest rate depending on the target for each year
    int_rate=sns.lineplot(data=df,x="issue_d", y="int_rate",hue="target")
    
    # Plot's axes title
    plt.ylabel("Interest rate", fontsize=13)
    plt.xlabel("Years", fontsize=13)
    
    # Give the variation of interest rate depending on the target 
    int_rate2=df.groupby(['target'])['int_rate'].describe()
    print(int_rate,int_rate2)
    
#############################################################################
# Graph 5 : Description of the loan amount and annual income of the applicant
#############################################################################


def target(df):
    
    # Describe function in order to get information on the target 
    # depending on the loan amount and annual income
    
    a=df.groupby(['target'])['loan_amnt'].describe()
    b=df.groupby(['target'])['annual_inc'].describe()
    print(a,b)
    
#############################################################################
############Graph 6 : Loans average amount per year #########################
#############################################################################

def loans_average(df):
    
    # Create a new variable which takes only the Year of the variable issue_d
    df['Year']= pd.DatetimeIndex(df['issue_d']).year

    # Define a list of our years
    cat = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017','2018']
    
    # Calculating the average loan amount per year   
    valeurs = [df[df["Year"].isin([2007])].loan_amnt.mean(),
           df[df["Year"].isin([2008])].loan_amnt.mean(),
           df[df["Year"].isin([2009])].loan_amnt.mean(),
           df[df["Year"].isin([2010])].loan_amnt.mean(),
           df[df["Year"].isin([2011])].loan_amnt.mean(),
           df[df["Year"].isin([2012])].loan_amnt.mean(),
           df[df["Year"].isin([2013])].loan_amnt.mean(),
           df[df["Year"].isin([2014])].loan_amnt.mean(),
           df[df["Year"].isin([2015])].loan_amnt.mean(),
           df[df["Year"].isin([2016])].loan_amnt.mean(),
           df[df["Year"].isin([2017])].loan_amnt.mean(),
           df[df["Year"].isin([2018])].loan_amnt.mean()]
            
    # Print the graph with its titles and axes
    sns.set_style("whitegrid")
    plt.figure(figsize=(10,4))
    y=plt.bar(cat, valeurs, color="green")
    plt.title("Titre : Loans average amount per year", fontsize=20)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Loan average amount", fontsize=15)    
    print(y)

