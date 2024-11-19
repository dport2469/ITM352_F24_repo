import matplotlib.pyplot as plt

x = list(range(0, 10))
y1 =  [e * 5 for e in x]
y2 =  [e * e for e in x]

plt.plot(x,y1)  # Plot some data on the Axes.
plt.scatter(x,y1)
plt.plot(x,y2)
plt.scatter(x,y2)
plt.title('Plot of 5x and x^2', fontsize=14)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)

plt.show()