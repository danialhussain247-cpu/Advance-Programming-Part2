import pandas as pd 
import unittest 
import cProfile
import Data_Ingestion

class Testing_csv_file(unittest.TestCase):
    def testing_load(self):
        file = Data_Ingestion.loading_csv()

        # check if the csv file exists
        self.assertIsNotNone(file)

        # checking if the file is not empty
        self.assertGreater(len(file), 0)
    

if __name__ == "__main__":
    unittest.main()


# using python pdb debugger, the below code we can easily retreive data by
# using simple commands in terminal such as "p file.head()" or "p file.columns"
file = pd.read_csv("Fitness_tracker_data_analysis.csv")
import pdb; pdb.set_trace()

#try block catch in loading csv file
try:
    file = pd.read_csv("Fitness_tracker_data_adnalysis.csv")
    print(file.columns)
except FileNotFoundError as e:
    print(e)

cProfile.run("""
file = pd.read_csv("Fitness_tracker_data_adnalysis.csv")
print(file.head())
         """)

# Create a test class that inherits from unittest.TestCase
class TestCSVLoading(unittest.TestCase):

    # This is the actual test method
    def test_csv_loads(self):
        # Try loading the CSV file into a DataFrame
        df = pd.read_csv("Fitness_tracker_data_adnalysis.csv")

        # Check that the DataFrame object was created (not None)
        self.assertIsNotNone(df)

        
        self.assertGreater(len(df), 0)
        

#  runs the test when the file is executed 
if __name__ == "__main__":
    unittest.main()

#running cProfile without def name




# using python pdb debugger 
file = pd.read_csv("mental_health_wearable_dataset.csv")
import pdb; pdb.set_trace() # this line opens debugger in terminal, we then can write
# pdb commands for csv file manipulation such as "p file.head()", or "p file.columns"
# or "p file.shape" for rows and coloumns and "p file.isnull().sum()" for missing values