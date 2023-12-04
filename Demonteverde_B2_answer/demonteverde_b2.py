import pandas as pd
import random as random
df = pd.read_csv('Exam_Table.csv') #added reading line
genusSt_rows = df[df['Genus'].to_string.startswith("St")] #defined condition for Genus starting w/ St
print (genusSt_rows) 
                   