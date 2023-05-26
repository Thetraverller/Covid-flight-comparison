import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "heathrowflightpassengerdataset120123.xlsx"
flights = pd.read_excel(file_path)

# Extract year and month from the 'Date' column
flights['Year'] = flights['Date'].dt.year
flights['Month'] = flights['Date'].dt.month

# Filter the data for years 2019 and 2022
filtered_flights = flights[(flights['Year'] == 2019) | (flights['Year'] == 2022)]

# Group the filtered data by year and month and calculate the sum of passengers for each combination
monthly_passengers = filtered_flights.groupby(['Year', 'Month'])['Heathrow_Passengers'].sum().unstack()

# Define the months as labels for the x-axis
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Get the unique years in the filtered data
years = filtered_flights['Year'].unique()

# Set the width of each bar
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = np.arange(len(months))
r2 = [x + bar_width for x in r1]

# Plot the bars
fig, ax = plt.subplots()
ax.bar(r1, monthly_passengers.loc[2019].values, width=bar_width, label='2019')
ax.bar(r2, monthly_passengers.loc[2022].values, width=bar_width, label='2022')

# Add labels, title, and legend
plt.xlabel('Month')
plt.ylabel('Passenger Count')
plt.title('Monthly Passengers at Heathrow Airport - 2019 vs 2022')
plt.xticks([r + bar_width/2 for r in range(len(months))], months)
plt.legend()

# Adjust the layout to prevent overlapping of labels
plt.tight_layout()

# Display the chart
plt.show()
