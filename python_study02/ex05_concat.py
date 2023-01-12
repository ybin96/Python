import pandas as pd
import numpy as np

group_a = pd.DataFrame({
    'id':[1,2,3,4,5],
    'test':[60,70,80,90,85]
})

group_b = pd.DataFrame({
    'id':[6,7,8,9,10],
    'test':[70,83,65,95,80]
})

print(group_a)
print(group_b)

group_all = pd.concat([group_a,group_b])
print(group_all)














