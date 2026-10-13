# Matplotlib All Important Graphs and Functions in One Program

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Sample Data
# -----------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 25, 30, 40])

students = ["Arun", "Bala", "Chitra", "Divya", "Ezhil"]
marks = [85, 90, 78, 88, 76]

subjects = ["Python", "Maths", "AI", "DBMS"]
percentage = [30, 25, 25, 20]

data = np.random.randn(100)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# -----------------------------
# Create Figure
# -----------------------------
plt.figure(figsize=(18, 16))

# 1. Line Plot
plt.subplot(4, 4, 1)
plt.plot(x, y, marker="o", label="Marks")
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

# 2. Bar Chart
plt.subplot(4, 4, 2)
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

# 3. Horizontal Bar Chart
plt.subplot(4, 4, 3)
plt.barh(students, marks)
plt.title("Horizontal Bar Chart")
plt.xlabel("Marks")
plt.ylabel("Students")

# 4. Pie Chart
plt.subplot(4, 4, 4)
plt.pie(percentage, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")

# 5. Scatter Plot
plt.subplot(4, 4, 5)
plt.scatter(x_scatter, y_scatter)
plt.title("Scatter Plot")
plt.xlabel("X Data")
plt.ylabel("Y Data")

# 6. Histogram
plt.subplot(4, 4, 6)
plt.hist(data, bins=10)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# 7. Box Plot
plt.subplot(4, 4, 7)
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")

# 8. Area Plot
plt.subplot(4, 4, 8)
plt.fill_between(x, y)
plt.title("Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 9. Step Plot
plt.subplot(4, 4, 9)
plt.step(x, y)
plt.title("Step Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 10. Stem Plot
plt.subplot(4, 4, 10)
plt.stem(x, y)
plt.title("Stem Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 11. Error Bar Plot
plt.subplot(4, 4, 11)
error = [2, 3, 1, 4, 2]
plt.errorbar(x, y, yerr=error, marker="o", capsize=5)
plt.title("Error Bar Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 12. Violin Plot
plt.subplot(4, 4, 12)
plt.violinplot(data)
plt.title("Violin Plot")
plt.ylabel("Values")

# 13. Stack Plot
plt.subplot(4, 4, 13)
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
c = [1, 3, 2, 4, 3]
plt.stackplot(x, a, b, c, labels=["A", "B", "C"])
plt.title("Stack Plot")
plt.xlabel("X Values")
plt.ylabel("Stacked Values")
plt.legend()

# 14. Heatmap
plt.subplot(4, 4, 14)
matrix = np.random.rand(5, 5)
plt.imshow(matrix)
plt.title("Heatmap")
plt.colorbar()

# 15. Multiple Lines
plt.subplot(4, 4, 15)
plt.plot(x, y, marker="o", label="Line 1")
plt.plot(x, y + 10, marker="s", label="Line 2")
plt.title("Multiple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

# 16. Text Annotation
plt.subplot(4, 4, 16)
plt.plot(x, y, marker="o")
plt.title("Annotation Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.annotate("Highest Point", xy=(5, 40), xytext=(3, 35),
             arrowprops=dict(arrowstyle="->"))
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Save the figure as image
plt.savefig("matplotlib_all_graphs.png")

# Display all plots
plt.show()


# -----------------------------
# Separate 3D Plot Example
# -----------------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

x3 = np.array([1, 2, 3, 4, 5])
y3 = np.array([2, 4, 6, 8, 10])
z3 = np.array([5, 10, 15, 20, 25])

ax.plot3D(x3, y3, z3, marker="o")
ax.set_title("3D Line Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()
