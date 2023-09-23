import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Line plots
ax.plot(x, y1, label='sin(x)', linestyle='-', color='b')
ax.plot(x, y2, label='cos(x)', linestyle='--', color='r')

# Scatter plot
scatter_x = np.random.rand(20) * 10
scatter_y = np.random.rand(20)
ax.scatter(scatter_x, scatter_y, label='Scatter', color='g', marker='o')

# Bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 30, 15, 40]
ax.bar(categories, values, label='Bar Chart', color='m')

# Histogram
data = np.random.randn(1000)
ax.hist(data, bins=30, label='Histogram', color='y', alpha=0.7)

# Annotations
ax.annotate('Peak', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(arrowstyle='->'))

# Titles and labels
ax.set_title('Sample Matplotlib Visualization')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Legends
ax.legend(loc='upper right')

# Grid
ax.grid(True, linestyle='--', alpha=0.6)

# Save the plot to a file
plt.savefig('sample_plot.png')

# Show the plot
plt.show()
