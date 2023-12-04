import pandas as pd
df = pd.read_csv("Exam_Table.csv") #added reading line
selected_rows = df.loc[:30] #selected rows from 0 to 30
print (selected_rows) #printing selected rows 0 to 30
    