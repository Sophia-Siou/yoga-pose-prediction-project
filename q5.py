import pandas as pd
import numpy as np
import math
import csv

df = pd.read_csv("test.csv", header=None)
df2 = df.copy()
del df2[0]
# write a dictionary about missing value can corresponding to the pose
miss_dict = {'bridge': 1, 'childs': 10, 'downwarddog': 12, 'mountain': 8,
             'plank': 9, 'seatedforwardbend': 4, 'tree': 2, 'warrior1': 3,
             'warrior2': 0}
tot_num = len(df2)
for row in range(0, tot_num):
    #print(row)
    miss_count = 0
    for col in df2:
        cell = df2.iloc[row][col]
        if cell == 9999:
            miss_count += 1

    for pose, miss in miss_dict.items():
        if miss_count == miss:
            cover = pose
            #print(pose)

    '''prediction = pd.read_csv("pred.csv")
    q5pred = open('pred5.csv', 'a', newline='')
    writer = csv.writer(q5pred)
    for item in prediction:
        if item == cover:
            writer.writerow([item])
        else:
            writer.writerow([cover])'''

# acccuracy
df3 = pd.read_csv("test.csv", header=None)
df4 = pd.read_csv("pred5.csv", header=None)
same = 0
count = 0
for i in df3[0] == df4[0]:
    count += 1
    if i == True:
        same += 1
print(same / count)