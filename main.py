import matplotlib.pyplot as plt
import pandas as pd
import csv

df = pd.read_csv("star_with_gravity.csv")
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.head()

name = df['Star_name'].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

name.sort()
mass.sort()
radius.sort()
dist.sort()
gravity.sort()

plt.scatter(name, mass)
plt.title("Name & Mass of the Star")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.show()

plt.scatter(name, radius)
plt.title("Name & Radius of the Star")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.show()

plt.scatter(name, dist)
plt.title('Name & Distance of the Star')
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

plt.scatter(name, gravity)
plt.title('Name & Gravity of the Star')
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.show()
