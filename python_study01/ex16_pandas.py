import pandas as pd
name = ['김지훈','이유진','박동현','김민지'];
english = [90,80,60,70]
math = [50,60,100,20]
df = pd.DataFrame({
    'name':name,
    'english':english,
    'math':math
})

# print(df)
print(df['english'])
print(sum(df['english']))
print(sum(df['math']))
print(sum(df['english'])/4)
print(sum(df['math'])/4)