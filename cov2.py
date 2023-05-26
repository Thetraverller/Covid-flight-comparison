import pandas as pd
import matplotlib.pyplot as plt

file_path = "heathrowflightpassengerdataset120123.xlsx"
flights = pd.read_excel(file_path)

# Convert 'Heathrow_Passengers' column to numeric
flights['Heathrow_Passengers'] = pd.to_numeric(flights['Heathrow_Passengers'], errors='coerce')

# Extract year and month from the 'Date' column
flights['Year'] = flights['Date'].dt.year
flights['Month'] = flights['Date'].dt.month

# Group the data by year
grouped_data = flights.groupby('Year')

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the line chart for each year
for year, group in grouped_data:
    ax.plot(group['Month'], group['Heathrow_Passengers'], label=year)

# Set the x-axis labels to show month names
month_names = pd.date_range(start='1/1/2023', periods=12, freq='M').strftime('%b')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_names)

ax.set_xlabel('Month')
ax.set_ylabel('Number of Passengers')
ax.set_title('Heathrow Airport Passenger Count by Year')
ax.legend()

ax.get_yaxis().get_major_formatter().set_scientific(False)  # Disable scientific notation

# Display the line chart
plt.show()
