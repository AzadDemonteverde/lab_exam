import pandas as pd

df = pd.read_csv("Exam_Table.csv")
pa_rows = df[df['Species'] == 'Pomacentrus adelus']
average_count = pa_rows['Count'].mean()

print ("Rows related to Pomacentrus adelus")
print ("pa_rows")
print ("\nAverage Count:", average_count)