import numpy as np
import pandas as pd
import xlrd

champs =pd.read_excel('./Data/MLB World Series Champions_ 1903-2016.xlsx')
print(champs)
print(type(champs))
#연습) 구단이름을 찾아보세요.   (중복된 이름은 제거)            완성하면 "3"
names = champs['Champion']
# print(names)
# print(type(names))
print(len(names))
names = list(set(names))
# print(names)
print(len(names))
names2 = champs.groupby('Champion').size().index
print(len(names2))
names3 = champs['Champion'].unique()
print(len(names3))
print("-"*50)

#연습) 우승팀들의 평균 승률을 출력 해봅니다.      완성하면 "3"
print(champs['WinRatio'].mean())
print(champs.WinRatio.mean())
a = champs.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
print(a)

#연습) 100승이상 승리한 팀들을 알려 주세요.         완성하면 "3"
over_100 = champs['Wins'] >= 100
print(over_100)
print(champs[over_100].Champion.unique())

print("-"*50)
#연습) New York Yankees의 평균 승률을 얼마입니까? 또, New York Yankees가 우승한 처음 연도와 마지막 연도를 구해 봅니다.
#                   완성하면 "3"
newyork = champs[champs['Champion'] == 'New York Yankees']
print(newyork)
print(newyork.WinRatio.mean())  #0.6386296296296295
print(newyork.iloc[0].Year)     #1923
print(newyork.iloc[-1].Year)    #2009
print("-"*50)
print(champs)

#연습) 최다 우승 top5를 골라 보세요.            완성하면 "1"
top_teams = champs.groupby('Champion').size()
top_teams = top_teams.sort_values(ascending=False)
print(top_teams)

fifth = top_teams[4]
print(fifth)
# print(top_teams >= fifth)
top_5 = top_teams[top_teams>=fifth]
print(top_5)

print('-'*50)

# a = np.arange(10)
# b = np.arange(5)
# print(a)
# print(b)
# print(np.setdiff1d(a,b))

#연습) 월드시리즈가 열리지 않은 연도를 찾아 보세요.      완성하면 "1"
# print(champs)
years = champs.Year.values
all_years = np.arange(1903, 2017)
print(years)
print(all_years)
print(np.setdiff1d(all_years,years))
# [1904 1994]



