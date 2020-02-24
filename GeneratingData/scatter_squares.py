import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

# set size of tick labels
plt.tick_params(axis="both", labelsize=14)
plt.show()
# plt.savefig('square_plot2.png', bbox_inches='tight')