import pandas as pd
df = pd.read_csv("Exam_Table.csv")
num_rows_to_extract = 31
extracted_rows = df.head(31)
print (extracted_rows)
    