import pandas as pd
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

# Plot the stacked bar chart
fig, ax = plt.subplots()
bottom = None
colors = plt.cm.get_cmap('tab10', len(years))  # Generate colors based on the number of years

for i, year in enumerate(years):
    data = monthly_passengers.loc[year].values
    ax.bar(months, data, bottom=bottom, label=str(year), color=colors(i))
    if bottom is None:
        bottom = data
    else:
        bottom += data

plt.xlabel('Month')
plt.ylabel('Passenger Count')
plt.title('Monthly Passengers at Heathrow Airport by Year')
plt.legend(title='Year')
plt.tight_layout()

# Display the chart
plt.show()
