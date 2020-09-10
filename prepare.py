import seaborn as sns
import pandas as pd
import numpy as np

# prep iris function
def prep_iris(idf):
    # naming dropping columns
    cols_to_drop = ['species_id', 'measurement_id']
    # dropping columns
    idf = idf.drop(columns = cols_to_drop)
    # renaming column
    idf.rename(columns={'species_name': 'species'}, inplace=True)
    # creating dataframe with dummy values
    dummy_df = pd.get_dummies(idf['species'], dummy_na = False)
    # adding dummy values DF to original DF
    idf = pd.concat([idf, dummy_df], axis=1)
    # returning new dataframe
    return idf

# prep titanic data
def prep_titanic(tdf):
    # importing for use
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.impute import SimpleImputer
    import warnings
    warnings.filterwarnings("ignore")
    # dropping column
    tdf = tdf.drop(columns = 'embark_town')
    # removing rows with empty embarked value
    tdf = tdf[~tdf.embarked.isnull()]
    # dropping column
    tdf = tdf.drop(columns = 'deck')
    # creating dataframe with dummy values
    dummy_df = pd.get_dummies(tdf['embarked'], dummy_na = False)
    # adding dummy values to original data frame
    tdf = pd.concat([tdf, dummy_df], axis=1)
    # creating variable that holds minmaxscaler function
    scaler = MinMaxScaler()
    # fitting and transforming data in age and far columns
    tdf[['age', 'fare']] = scaler.fit_transform(tdf[['age', 'fare']])
    # setting variable with simple imputer set to most frequent
    imputer = SimpleImputer(strategy = 'most_frequent')
    # filling all age values that were empty with most frequent value from age column
    imputer = imputer.fit(tdf[['age']])
    tdf[['age']] = imputer.transform(tdf[['age']])
    # returning DF
    return tdf
