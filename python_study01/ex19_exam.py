import pandas as pd
exam = pd.read_csv('../Data/exam.csv')
print(exam.head(1))
print(exam.tail(1))
print(exam.shape)
print(exam.info())
print(exam.describe())