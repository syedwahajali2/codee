import matplotlib.pyplot as plt

categories = ["Food", "Transport", "Education", "Shopping", "Bills"]
expenses = [8500, 3000, 5000, 4200, 6500]

total = sum(expenses)
largest_category = categories[expenses.index(max(expenses))]

plt.figure(figsize=(7, 7))
plt.pie(expenses, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("Monthly Expense Breakdown")
plt.tight_layout()
plt.savefig("expense_breakdown.png")
plt.show()

print("Total expenses: PKR", total)
print("Highest spending category:", largest_category)
