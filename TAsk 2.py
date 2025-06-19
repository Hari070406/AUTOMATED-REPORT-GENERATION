import pandas as pd
data = pd.read_csv("data.csv")
print(data)
average_marks = data["Marks"].mean()
print("Average Marks:", average_marks)
