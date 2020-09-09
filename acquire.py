# Make a function named get_titanic_data that returns the titanic data from the codeup data science database 
# as a pandas data frame. 
# Obtain your data from the Codeup Data Science Database.

# importing env for access to user, host and password
import env

# creating function that returns a path that can be used to connect to SQL database
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

# creating function that creates query for SQL titanic data and then uses the previous function 
# to connect to the database and return the passengers data as a dataframe
def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

# display data frame
get_titanic_data()

# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database 
# as a pandas data frame. The returned data frame should include the actual name of the species in addition to 
# the species_ids. Obtain your data from the Codeup Data Science Database.

# creating function that creates query for SQL iris data and then uses the get_connection function 
# to connect to the database and return the iris data as a dataframe
def get_iris_data():
    return pd.read_sql('SELECT * FROM measurements AS m JOIN species USING (species_id)', get_connection('iris_db'))

# display data frame
get_iris_data()

# Once you've got your get_titanic_data and get_iris_data functions written, 
# now it's time to add caching to them. To do this, edit the beginning of the function to check for a 
# local filename like titanic.csv or iris.csv. If they exist, use the .csv file. 
# If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the 
# dataframe to a .csv file with the appropriate name.

# importing os for use in function
import os

# creating function that creates a variable call filename that holds the name of a current, or soon to be created file
def new_get_titanic_data():
    filename = "titanic.csv"
    # if a file is found with a name that matches filename (titanic.csv), the function will return the data as a dataframe
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    # if no file with the specified name can be found the else statement is ran
    else:
        # creating sql query and using get_connection function to connect to titanic database and create
        # dataframe using data in passengers table
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

        # writing dataframe to csv file
        df.to_csv(filename, index = False)

        # return the dataframe
        return df 

# importing os for use in function (was done earlier but displaying here to clarity)
import os

# creating function that creates a variable call filename that holds the name of a current, or soon to be created file
def new_get_iris_data():
    filename = "iris.csv"
    
     # if a file is found with a name that matches filename (iris.csv), the function will return the data as a dataframe
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    # if no file with the specified name can be found the else statement is ran
    else:
        # creating sql query and using get_connection function to connect to iris database and create
        # dataframe using data in measurements table joined with species table
        df = pd.read_sql('SELECT * FROM measurements AS m JOIN species USING (species_id)', get_connection('iris_db'))

        # writing dataframe to csv file
        df.to_csv(filename, index = False)

        # return the dataframe
        return df 