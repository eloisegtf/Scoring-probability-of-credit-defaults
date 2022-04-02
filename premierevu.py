#Importation of the librairies that we will need in this module
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#This option will allow us to see all the columns of the data
pd.options.display.max_columns=None

#The function get_file allows us to enter the path where the base is and charge it 
def get_file() :
    path=input("Enter the path where the database is located :") 
    df=pd.read_csv(path+'accepted_2007_to_2018Q4.csv')
    return df

#The function apercu allow us to know the dimension of the data base and see the first rows of it
#It takes as input the data base df
def apercu (df) :
    dim=df.shape
    print("The shape of the base is :", dim)
    prem=df.head()
    return prem

#The function takes as input the data base df and return the number of duplicated in the base
def doublons (df):
    doublons=df.duplicated().sum()
    print("The number of duplicated is :", doublons)
    
#The function p_v will be call in the principal script
#It print the results of the two functions created before
def p_v(df):
    print(apercu(df))
    print(doublons(df))

#The function call for function which doesn't have input are in if main
#Like that the function won't be run when the import of the module will be done
if __name__ == "__main__" :
    get_file()
