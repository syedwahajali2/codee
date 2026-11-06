import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 15000, 13500, 18000, 22000, 20000]
expenses = [7000, 8000, 7500, 9500, 11000, 10500]

# Calculate profit
profit = [sales[i] - expenses[i] for i in range(len(months))]

# Create a figure with three charts
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Bar chart: Sales by month
axes[0].bar(months, sales)
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales (PKR)")

# 2. Line chart: Expenses by month
axes[1].plot(months, expenses, marker="o")
axes[1].set_title("Monthly Expenses")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Expenses (PKR)")

# 3. Pie chart: Total sales and expenses
total_sales = sum(sales)
total_expenses = sum(expenses)
axes[2].pie(
    [total_sales, total_expenses],
    labels=["Sales", "Expenses"],
    autopct="%1.1f%%",
    startangle=90
)
axes[2].set_title("Sales vs Expenses")

# Add a main title and adjust spacing
fig.suptitle("Business Sales Report", fontsize=16)
plt.tight_layout()

# Save the chart as an image and display it
plt.savefig("sales_report.png", dpi=300, bbox_inches="tight")
plt.show()

# Print a simple summary
print("Total Sales:", total_sales)
print("Total Expenses:", total_expenses)
print("Total Profit:", sum(profit))
