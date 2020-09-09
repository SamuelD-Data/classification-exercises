import seaborn as sns
import pandas as pd
import numpy as np

# prep iris function
def prep_iris(idf):
    cols_to_drop = ['species_id', 'measurement_id']
    idf = idf.drop(columns = cols_to_drop)
    idf.rename(columns={'species_name': 'species'}, inplace=True)
    dummy_df = pd.get_dummies(idf['species'], dummy_na = False)
    idf = pd.concat([idf, dummy_df], axis=1)
    return idf
    
# prep titanic function
def prep_titanic(tdf):
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.impute import SimpleImputer
    import warnings
    warnings.filterwarnings("ignore")
    
    tdf = tdf.drop(columns = 'embark_town')
    tdf = tdf[~tdf.embarked.isnull()]
    tdf = tdf.drop(columns = 'deck')
    dummy_df = pd.get_dummies(tdf['embarked'], dummy_na = False)
    tdf = pd.concat([tdf, dummy_df], axis=1)
    scaler = MinMaxScaler()
    scaler.fit(tdf[['age']])
    age_scaler = scaler.transform(tdf[['age']])
    tdf['age_scaled'] = age_scaler
    scaler.fit(tdf[['fare']])
    fare_scaler = scaler.transform(tdf[['fare']])
    tdf['fare_scaled'] = fare_scaler 
    imputer = SimpleImputer(strategy = 'most_frequent')
    imputer = imputer.fit(tdf[['age']])
    tdf[['age']] = imputer.transform(tdf[['age']])
    return tdf

