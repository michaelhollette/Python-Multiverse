import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Generating data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creating a line plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="Sine Wave", color="blue", linestyle="--")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")
plt.legend()
plt.show()

# Generating data
x = np.random.rand(50)
y = np.random.rand(50)

# Creating a scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color="purple", marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot Example")
plt.show()

# Generating data
data = np.random.normal(0, 1, 1000)

# Creating a histogram
plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color="orange", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()


###### Seaborn ######

# Generating data
tips = sns.load_dataset("tips")

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time", size="size")
plt.title("Scatter Plot with Seaborn")
plt.show()

# Creating a histogram with KDE
plt.figure(figsize=(8, 4))
sns.histplot(data, bins=30, kde=True, color="teal")
plt.title("Histogram with Seaborn")
plt.show()

# Creating a correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(tips.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap with Seaborn")
plt.show()

# Pair plot
sns.pairplot(tips, hue="day", markers=["o", "s", "D", "^"])
plt.suptitle("Pair Plot Example", y=1.02)
plt.show()
