import pandas as pd
df = pd.read_csv ('Exam_Table.csv')

transposed_df = df.transpose()
transposed_df.to_csv('ExamTable_transposed.csv')

print ("transposed_df")