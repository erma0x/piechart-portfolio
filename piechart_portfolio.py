import pandas as pd
import matplotlib.pyplot as plt
import sys

path_file = sys.path[0]

df = pd.read_csv(path_file+"/investiments.csv")

data = df.groupby("type")["value"].sum()
data2 = df["value"]

fig, axs = plt.subplots(2)
fig.suptitle('My Portfolio')

axs[0].pie(data,labels=df["type"].unique())

plt.title('by name')
axs[1].pie(data2,labels=df["name"])

plt.show()
