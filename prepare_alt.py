# ################ NOTE: The functions below are only for us in the model exercises as they differ from the functions first created in the data_preperation exercises
# ################ Please see "prep.py" for the correct functions to the data preperation exercises

import pandas as pd
import numpy as np
import scipy as sp 
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

# creating function to split data into train, validate and test DFs
def train_valid_test(df):
    train_validate, test = train_test_split(df, test_size = .2, random_state = 123, stratify = df.survived)
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123, stratify = train_validate.survived)
    return train, validate, test

# creating function to prep titanic data 
def prep_titanic(df):
    # dropping unnecesary columns
    df.drop(columns = ['class', 'passenger_id', 'deck'], inplace = True)
    # convert sex to category type
    df["sex"] = df["sex"].astype("category")
    # adding sex category to DF
    df["categorical_sex"] = df["sex"].cat.codes
    # convert embark_town to category type
    df["embark_town"] = df["embark_town"].astype('category')
    # adding embark_town category to DF
    df["embark_town"] = df["embark_town"].cat.codes
    # returnining DF
    return df
