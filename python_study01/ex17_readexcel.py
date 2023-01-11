import pandas as pd


df_exam = pd.read_excel("../Data/excel_exam.xlsx", sheet_name='sist')
print(df_exam)

df_exam1 = pd.read_excel("../Data/excel_exam.xlsx")
print(df_exam1)




# df_exam_novar = pd.read_excel("../Data/excel_exam_novar.xlsx", header=None)
# print(df_exam_novar)
# print(len(df_exam_novar))



# df_exam = pd.read_excel('../Data/excel_exam.xlsx')
# print(df_exam)
#
# print(sum(df_exam['english'])/len(df_exam))
# print(sum(df_exam['science'])/len(df_exam))

# x = [1,2,3,4,5]
# print(x)
# print(len(x))
#
# df = pd.DataFrame({
#     "a":[1,2,3],
#     "b":[4,5,6]
# })
# print(df)
# print(len(df))