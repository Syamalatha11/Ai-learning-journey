# Matplotlib Basics to Advanced

import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# 3. Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# 4. Pie Chart
sizes = [40, 30, 20, 10]
labels = ["Python", "Java", "C", "JavaScript"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()

# 5. Histogram
data = [12, 15, 18, 20, 22, 25, 25, 28, 30]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()
