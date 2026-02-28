import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# 1. Load the CSV
df = pd.read_csv('energy_data.csv')

# 2. Calculate Total Energy Consumed (Watt-hours)
# Using the Trapezoidal rule for integration (Area under the Power curve)
# We assume a 0.5s interval based on the Arduino delay(500)
time_interval_hours = 0.5 / 3600 
total_watt_hours = np.trapezoid(df['Power_Watts'], dx=time_interval_hours)

# 3. Create the Visualization
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Power_Watts'], color='red', linewidth=2, label='Real-time Power')

# Styling the graph for a professional report
plt.title(f'Energy Consumption Profile\nTotal Energy Used: {total_watt_hours:.4f} Wh', fontsize=14)
plt.xlabel('Time (HH:MM:SS)', fontsize=12)
plt.ylabel('Power (Watts)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
# Only show every 20th label so they don't overlap
ax = plt.gca() # Get current axis
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
plt.show()