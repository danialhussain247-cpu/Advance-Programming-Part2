import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
#-----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------Daily Steps Graph ---------------------------------------------------------------------------
# loading the csv file 
file = pd.read_csv("Fitness_tracker_data_analysis.csv")

# graph for daily steps 
plt.figure(figsize=(6,5)) # canvas size
sns.lineplot(x="On average, do you reach your daily step goal? "
, y="Do you set a daily step goal on your tracker? ", data=file.head(200)) # x and y coloums and then file name
plt.title("Average steps count Graph: ") # title
plt.xticks(rotation=70) # rotation
plt.tight_layout() # organising

plt.show() # displaying

#--------------------------------------------------------------------------------Sleep Quality Score Graph ---------------------------------------------------------------------
# loading the csv file 
file = pd.read_csv("Fitness_tracker_data_analysis.csv")


plt.figure(figsize=(6,5))
sns.countplot(x="How many minutes of exercise do you complete daily (based on your tracker)? ", data=file.head(200))
plt.title("Sleep Duration Graph: ")
plt.xlabel("Average time you exersice: ")
plt.ylabel("Sleep Duration: ")

plt.show()
#----------------------------------------------------------------------------------Heart Rate Graph ----------------------------------------------------------

# loading the csv file 
file = pd.read_csv("Fitness_tracker_data_analysis.csv")

plt.figure(figsize=(5,6))
sns.countplot(x="What brand of fitness tracker do you use? " , data=file)
plt.title("Companies: ")
plt.xlabel("Brands: ")
plt.ylabel("Users: ")

plt.show()