import pandas as pd
import sqlite3
#---------------------------------------------------------------------------------------------------------------------------------------------

# loading the csv file 
def loading_csv(): # def function of loading the csv file
    return pd.read_csv("Fitness_tracker_data_analysis.csv") # return makes it so we can use elsewhere
# this will run the code but also be easy for testing
if __name__=="__main__":
    file = loading_csv()
    
print("Print first few rows: ")
print(file.head())
print("printing entire coloumns names: ")
print(file.columns)

print("-" * 100)

# exploring and cleaning the csv data
# checking the basic information of csv
print("Checking the basic information of csv file: ")
file.info()
# checking to determine the null values from csv file
print("Checking the null values from the csv file: ")
print(file.isnull().sum())
# from these two commmands the csv file does looks clean
# selecting the relevant coloums 
relevant_columns = ["Gender ",
                    "Do you use a fitness tracker daily? ",
                    "What brand of fitness tracker do you use? ",
                    "Do you set a daily step goal on your tracker? ",
                    "Do you monitor your sleep using your fitness tracker? ",
                
                
                ]
# getting rid of irrelevant coloums and creating new file sample
new_file = file[relevant_columns].dropna()
# check basic info
print("Cheking basic infomation of new file: ")
print(new_file.info())
# checking if all the coloums were selected and irrelevent are dropped
print("See the selected coloums: ")
print(new_file.columns)

# Database 
# creating a database 
print("Creating a database for the new file: ")
conn = sqlite3.connect("fitness_tracker.db")
# strong the new file to the database
new_file.to_sql("user_activity", conn , if_exists="replace", index=False)
print("The new file has been strored into a new databse: ")
# verification of database
print("verifying the connection to database: ")
query1 ="SELECT * FROM user_activity LIMIT 4"

result = pd.read_sql(query1, conn)
print("Printing the content from the database: ")
print(result)