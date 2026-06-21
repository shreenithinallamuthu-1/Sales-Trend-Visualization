import os
import matplotlib.pyplot as plt
import pandas as pd

# 1. Setting up our days of the week
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
sales_data = []

print("--- Welcome to the Advanced Sales Trend Reporter ---")
print("Please enter the sales amount (₹) for each day:\n")

# 2. Loop through each day and ask the user for data
for day in days:
    while True:
        try:
            user_input = input(f"Enter sales for {day} (₹): ")
            amount = float(user_input)
            sales_data.append(amount)
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# 3. Put data into a DataFrame and save it to your Desktop
df = pd.DataFrame({"Day": days, "Sales": sales_data})

desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
csv_filename = os.path.join(desktop_path, "weekly_sales.csv")
df.to_csv(csv_filename, index=False)

# 4. Calculate Weekly Summary Statistics
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()

# Find rows with max and min sales
max_row = df.loc[df["Sales"].idxmax()]
min_row = df.loc[df["Sales"].idxmin()]

print("\n" + "=" * 40)
print("📋 WEEKLY SALES SUMMARY")
print("=" * 40)
print(f"Total Weekly Sales : ₹{total_sales:,.2f}")
print(f"Average Daily Sales: ₹{avg_sales:,.2f}")
print(f"Highest Sales Day  : {max_row['Day']} (₹{max_row['Sales']:,.2f})")
print(f"Lowest Sales Day   : {min_row['Day']} (₹{min_row['Sales']:,.2f})")
print("=" * 40)

print("\n💡 SIMPLE INSIGHTS:")
print(f"• Highest sales were recorded on {max_row['Day']}.")
print(f"• Lowest sales were recorded on {min_row['Day']}.")
print(f"• Your business averaged ₹{avg_sales:,.2f} per day this week.")
print("-" * 40)
print(f"💾 CSV Saved to Desktop: weekly_sales_data.csv")
print("📊 Generating your charts... close the window to exit.")

# 5. Create Dual Visualizations (Line Chart + Bar Chart side-by-side)
# Creating a canvas with 1 row and 2 separate chart columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# --- CHART 1: LINE CHART ---
ax1.plot(
    df["Day"],
    df["Sales"],
    marker="o",
    color="g",
    linestyle="-",
    linewidth=2,
    label="Sales Trend",
)
ax1.set_title("Weekly Sales Trend (Line)", fontsize=13, fontweight="bold")
ax1.set_xlabel("Day of the Week", fontsize=11)
ax1.set_ylabel("Sales (₹)", fontsize=11)  # Clear Rupee Label
ax1.grid(True, linestyle="--", alpha=0.5)

# Show values near each point on the Line Chart
for i, txt in enumerate(df["Sales"]):
    ax1.annotate(
        f"₹{txt:,.0f}",
        (df["Day"][i], df["Sales"][i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        fontweight="bold",
        color="darkgreen",
    )

# --- CHART 2: BAR CHART ---
bars = ax2.bar(df["Day"], df["Sales"], color="skyblue", edgecolor="navy")
ax2.set_title("Daily Sales Comparison (Bar)", fontsize=13, fontweight="bold")
ax2.set_xlabel("Day of the Week", fontsize=11)
ax2.set_ylabel("Sales (₹)", fontsize=11)  # Clear Rupee Label
ax2.grid(True, linestyle="--", alpha=0.3, axis="y")

# Show values on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        yval + (max(sales_data) * 0.01),
        f"₹{yval:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold",
    )

# Rotate labels slightly if they crowd together
fig.autofmt_xdate()

# 6. Display everything beautifully
plt.tight_layout()
plt.show()
