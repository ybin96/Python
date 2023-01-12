import pandas as pd
import numpy as np

group_a = pd.DataFrame({
    'id':[1,2,3,4,5,6,7],
    'test':[60,70,80,90,85,100,100]         #<---- 6,7번이 중복이 되는데 중복하여 합쳐 줍니다.
})

group_b = pd.DataFrame({
    'id':[6,7,8,9,10],
    'test':[70,83,65,95,80]
})

print(group_a)
print(group_b)

group_all = pd.concat([group_a,group_b])
print(group_all)














