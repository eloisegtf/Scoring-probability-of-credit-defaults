# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:45:42 2021

@author: elois
"""
#Importation of the librairies that we will need in this module
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import tri as tr
import matplotlib as plt
import seaborn as sns

#This function takes as input the data base, the names of the columns that we want to target enconding, the name of the target and the weight
def target_encoding_lisse(data, by, on, m):
    # Compute the men of the target
    mean = data[on].mean()
    # Compute the number of values and the mean of each group
    agg = data.groupby(by)[on].agg(['count', 'mean'])
    counts = agg['count']
    means = agg['mean']
    # Compute the "smoothed" means
    smooth = (counts * means + m * mean) / (counts + m)
    # Replace each value by the according smoothed mean
    return data[by].map(smooth)

#This function allows us to apply the target encoding on our variables which have the type object and on the variable 'hardship_plan_binary'that we changed
#We don't enconding the variable 'target' and 'issue_d'
def use_target (df):
    df['hardship_plan_binary']=target_encoding_lisse(df, 'hardship_plan_binary', on='target', m=10)
    for col in df.select_dtypes('object') :
        if col!='issue_d' or col!='target':       
            by=col
            df[col]=target_encoding_lisse(df, by , on='target', m=10)

#This function caculat the VIF 
def calcul_vif(X):
    vif=pd.DataFrame()
    vif['Variables']=X.columns
    vif['VIF']=[variance_inflation_factor(X.values,i) for i in range(X.shape[1])]
    return(vif.sort_values(by=['VIF'],ascending=False))

#This function call the function which use the target enconding
#It created a copy of our data base without the variable which doesn't have the numeric type
#We call the VIF and makes a graph of it
def selectvar(df):
    use_target(df)
    df2=df.copy(deep=True)
    del(df2['issue_d'])
    X = df2.iloc[:,:]
    vif=calcul_vif(X).head(22)['Variables'] 
    plt.figure(figsize=(8,6))
    pgreen=sns.diverging_palette(145, 300, s=60, as_cmap=True)
    mask= (-0.40 < df2[vif].corr()) & (df2[vif].corr() < 0.40)
    mask[mask]=True
    sns.heatmap(df2[vif].corr(), annot=True, cmap=pgreen,mask=mask)
    
#This function takes as input the data base
#It creates variables that represent the mean of other variables.
#It removes variables that are highly correlated.
def changevar_vif(df):
    df['fico_range_mean']=df['fico_range_low'].mean() + df['fico_range_high'].mean()
    df['sec_app_fico_range_mean']=df['sec_app_fico_range_low'].mean() + df['sec_app_fico_range_high'].mean()
    tr.drop_cols(df,['sec_app_fico_range_low','sec_app_fico_range_high','fico_range_high','fico_range_low'])
    tr.drop_cols(df,['sec_app_chargeoff_within_12_mths','sec_app_mort_acc','installment','num_sats',
                     'tot_hi_cred_lim','sub_grade','total_bc_limit'])
    tr.drop_cols(df,['level_0','tot_cur_bal','num_actv_bc_tl','num_bc_sats',
                     'sec_app_collection_12_mths_ex_med'])



    