import pandas as pd
import numpy as np

test1 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'midterm':[60,80,70,90,85]
})

test2 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'final':[70,83,65,95,80]
})

print(test1)
print(test2)

total = pd.merge(test1, test2, on="id")
print(total)












