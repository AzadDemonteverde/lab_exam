import pandas as pd
df = pd.read_csv("Exam_Table.csv")
selected_rows = df.loc[:30]
print (selected_rows)
    