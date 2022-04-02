# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:05:28 2021

@author: elois
"""
#This function allow us to delete a column in df 
#It will be use a lot of time in this module or call in other module
def drop_cols(df,cols):
    df.drop(labels=cols, axis=1, inplace=True, errors='ignore')
        
#This function print for each columns which have a type Object, the number of modalities for this variable
def nbrmod (df) :
    for col in df.select_dtypes('object'):
        print(f'The column {col} has {df[col].nunique()} modalities.')

#We create a list with the name of variables which have a lot of modalities    
list_tropmod = ['id','emp_title','title','zip_code','url', 'desc','earliest_cr_line', 'sec_app_earliest_cr_line']

#We create a list with the name of variables that we don't need to know
list_noneed = [ 'debt_settlement_flag', 'disbursement_method', 
             'funded_amnt', 'funded_amnt_inv', 'inq_last_6mths',
            'last_credit_pull_d', 'last_fico_range_high', 
             'last_fico_range_low', 'last_pymnt_amnt', 
             'last_pymnt_d','mo_sin_rcnt_rev_tl_op', 
            'mo_sin_rcnt_tl', 'mths_since_recent_bc', 
            'mths_since_recent_inq','num_op_rev_tl',
             'num_rev_accts', 'num_rev_tl_bal_gt_0', 
             'num_tl_30dpd','out_prncp', 
             'out_prncp_inv', 'pymnt_plan', 'recoveries', 
           'tax_liens', 'tot_coll_amt',  'total_il_high_credit_limit', 
             'total_pymnt', 
             'total_pymnt_inv', 
             'total_rec_int', 
             'total_rec_late_fee',
             'total_rec_prncp', 
             'total_rev_hi_lim', 'next_pymnt_d','inq_last_12m','sec_app_num_rev_accts','collection_recovery_fee']

#We create a list with the name of variables which have a lot of zero
list_tropzero=['collections_12_mths_ex_med','acc_now_delinq','open_il_24m','open_rv_24m','max_bal_bc','inq_fi',
               'total_cu_tl','delinq_amnt','num_accts_ever_120_pd','num_il_tl','num_tl_90g_dpd_24m','bc_util']

#The function first_sup takes as input the data base
#It allows us to delete the variables in the three list using the function drop_cols
def first_sup (df):
    print(nbrmod(df))
    drop_cols(df,list_tropmod)
    drop_cols(df,list_noneed)
    drop_cols(df,list_tropzero)

#We create a list with the name of variables which have more than 80% of missing values
list_tropna = ['orig_projected_additional_accrued_interest', 'member_id',
              'hardship_type' , 'hardship_reason', 'hardship_status', 
              'hardship_last_payment_amount', 
                'hardship_payoff_balance_amount','hardship_loan_status'  ,    
            'hardship_dpd','hardship_length', 'payment_plan_start_date',
              'hardship_start_date', 'hardship_end_date', 'hardship_amount', 
              'settlement_percentage', 'settlement_term', 
              'debt_settlement_flag_date', 'settlement_amount',
                'settlement_date', 
                'settlement_status', 'sec_app_revol_util', 
              'sec_app_open_act_il', 'sec_app_open_acc',
              'sec_app_inq_last_6mths',  
              'mths_since_last_record', 'mths_since_recent_bc_dlq',       
                'mths_since_last_major_derog', 'mths_since_recent_revol_delinq', 'annual_inc_joint', 'dti_joint', 'verification_status_joint']

#We cretae three différent list of variables which have less than 80%
#Each list will have a different gestion of their missing values
liste_bcpna=['sec_app_mths_since_last_major_derog', 'revol_bal_joint', 'sec_app_chargeoff_within_12_mths', 'sec_app_collections_12_mths_ex_med', 'sec_app_mort_acc', 'sec_app_fico_range_high', 'sec_app_fico_range_low']

liste_peuna=['mths_since_last_delinq', 'mths_since_rcnt_il', 'num_tl_120dpd_2m', 'mo_sin_old_il_acct', 'pct_tl_nvr_dlq', 'avg_cur_bal', 'il_util', 'all_util', 'emp_length','mths_since_rcnt_il','num_bc_sats','num_sats','total_bal_ex_mort','mort_acc','acc_open_past_24mths','total_bc_limit','revol_util','pub_rec_bankruptcies','dti','chargeoff_within_12_mths']

liste_minna = ['open_act_il', 'open_acc_6m', 'open_rv_12m','open_il_12m','mo_sin_old_rev_tl_op', 
         'bc_open_to_buy', 'num_actv_rev_tl', 'tot_cur_bal','num_actv_bc_tl', 'num_bc_tl', 'percent_bc_gt_75',
          'num_tl_op_past_12m', 'tot_hi_cred_lim', 'num_bc_tl','total_bal_il']

#This function takes as input a fuction and list of variables
#It will replace the missing values of the variables in the list with -10 if the variables are of type float
def gestion_bcpna (data,listvar):
    n=len(listvar)
    i=0
    for i in range(0,n) :
        if data[listvar[i]].dtypes==float :
            data[listvar[i]].fillna(-10,inplace=True)

#This function takes as input a fuction and list of variables
#It will replace the missing values of the variables in the list with the mean of it if the variables are of type float
#If the variable has an object type it will replace the issing valeues by a new modalities named "Unknown"
def gestion_peunan (data, listvar):
    i=0
    n=len(listvar)
    for i in range (0,n) :
        if data[listvar[i]].dtypes==float :
            moy=data[listvar[i]].mean()
            data[listvar[i]].fillna(moy, inplace=True)
        if data[listvar[i]].dtypes==object : 
            data[listvar[i]].fillna("unknown", inplace=True)

#This function takes as input a fuction and list of variables
#It will replace the missing values of the variables in the list with the minimum of it 
def gestion_minna (data, listvar):
    i=0
    n=len(listvar)
    for i in range (0,n) :
        mini=data[listvar[i]].min()
        data[listvar[i]].fillna(mini, inplace=True)

#This function takes as input the data base 
#We call in it all the function created for the gestion of the missing values apply to the lists
def gestion_na (df) :
    print('The percentage of missing values is : ', (df.isna().sum()/df.shape[0]).sort_values(ascending=False).head(60))
    drop_cols(df,list_tropna)
    gestion_bcpna(df,liste_bcpna)
    gestion_peunan(df,liste_peuna)
    gestion_minna(df,liste_minna)
    varrest=df.shape 
    print("The new shape of the base is :",varrest)