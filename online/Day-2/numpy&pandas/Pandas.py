import pandas as pd

# Sample data (Ensure column names match the dataset exactly)
data = {
    "Project": ["Solar Farm", "Wind Turbine", "Hydropower", "Solar Roof", "Geothermal Plant"],
    "Location": ["USA", "Germany", "India", "China", "Australia"],
    "Capacity(MW)": [150, 200, 90, 120, 180],
    "cost (Millions $)": [300, 500, 180, 240, 400],
    "Completion Year": [2023, 2024, 2022, 2025, 2023]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Green Technology Project DATA Frames:\n", df)

# Filter projects with capacity greater than 100 MW
hcp = df[df['Capacity(MW)'] > 100]
print("\nProjects with Capacity > 100MW:\n", hcp)

# Calculate cost per MW
df["Cost per MW"] = df["cost (Millions $)"] / df["Capacity(MW)"]
print("\nDataFrame with Cost per MW:\n", df)

# Aggregation: Total Capacity and Cost
total_capacity = df['Capacity(MW)'].sum()
total_cost = df["cost (Millions $)"].sum()
print("\nTotal Capacity of all projects:", total_capacity, "MW")
print("Total Cost of all projects: $", total_cost, "Million")

# Grouping: Aggregate data by Location
grouped_data = df.groupby("Location").agg({
    "Capacity(MW)": "sum",
    "cost (Millions $)": "sum",
    "Cost per MW": "mean"
}).reset_index()

print("\nGrouped Data by Location:\n", grouped_data)
