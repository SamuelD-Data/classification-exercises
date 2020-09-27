# notes for classification project 

# prepare

Prepared data for exploration via:

     Addressing missing values

     Identifying outliers

     Converting data to numerical format

     Dropping duplicate rows

Creating new column denoting whether customer used automatic vs manual payments

Changing "no_phone_service value in columns to "No"

Changing "no_internet_service value in columns to "No"

Converting "No" values to 0

Converting "Yes" values to 1

Renaming "tenure" column to "monthly_tenure"

Creating column that holds tenure in years

Converting "total_charges" from object to float

Splitting data into train, validate, test

# explore

created heatmap of every variable's correlation to churn

identified 4 driver variables with strongest correlation (monthly charges, dependents, partner, automatic payments)

plotted monthly charges, dependents, partner and automatic payements vs tenure to see if any of them correlates with retention

performed t-tests and confirmed tenure is longer on average when:
     monthly charges were lower
     customer had dependents
     customer had partner
     customer used automatic payments

# modeling

Created baseline model and checked accuracy against train dataset

Created 3 alternate models

Model 1
KNearestNeighbor
Neighbors = 3
Uses all 4 driver variables

Model 2
Decision Tree
Max Depth = 2
Uses monthly charges and automatic payments

Model 3
Logistic Regression
Uses all 4 driver variables

Made predictions for training dataset using all four models
Models 1 and 3 performed the best with regard to accuracy

Made predictions for validation dataset using models 1 and 3
Model 3 performed the best with regard to accuracy

Made predictions for test dataset using models 3
Model 3's accuracy was acceptable (73%)



