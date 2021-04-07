import pandas as pd
import numpy as np
import math
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv", header=None)
df = df.replace(9999, np.nan)
gb = df.groupby(0)
data = gb.get_group('bridge')
data.hist()
plt.savefig("q2 histogram.png")
plt.show()
