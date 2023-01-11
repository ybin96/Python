import pandas as pd

# df_csv_exam = pd.read_csv('../Data/exam.csv')
# print(df_csv_exam)

df_midterm = pd.DataFrame({
    'english':[90,80,60,70],
    'math':[50,60,100,20],
    'nclass':[1,1,2,2]
})

print(df_midterm)
df_midterm.to_csv("../Data/output_newdata.csv",index=False)

