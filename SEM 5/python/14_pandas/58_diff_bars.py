import matplotlib.pyplot as plt

drivers = ['Max Verstappen', 'Sergio Perez', 'Lewis Hamilton', 'Fernando Alonso', 'Charles Leclerc']
points = [454, 275, 240, 209, 206]
races_won = [18, 2, 1, 0, 1]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# ! 1 Bar plot for points
ax1.bar(drivers, points, color=['blue','darkred','silver','green','red'], width=0.6)
ax1.set_title('F1 2023 Driver Points')
ax1.set_xlabel('Drivers')
ax1.set_ylabel('Points')

# ! 2 Line plot for races won
ax2.plot(drivers, races_won, color='green', marker='o', linestyle='--')
ax2.set_title('F1 2023 Race Wins')
ax2.set_xlabel('Drivers')
ax2.set_ylabel('Races Won')

# ! 3 Pie chart for races won distribution
ax3.pie(races_won, labels=drivers, autopct='%1.1f%%', startangle=90, colors=['blue', 'orange', 'green', 'red', 'purple'])
ax3.set_title('F1 2023 Race Wins Distribution')

# ! 4 Scatter plot for points vs races won
ax4.scatter(points, races_won, color='purple', edgecolor='black', s=100)
for i, driver in enumerate(drivers):
    ax4.annotate(driver, (points[i], races_won[i]), textcoords="offset points", xytext=(0,10), ha='center')

ax4.set_title('F1 2023 Points vs Races Won')
ax4.set_xlabel('Points')
ax4.set_ylabel('Races Won')

plt.tight_layout()

plt.show()
